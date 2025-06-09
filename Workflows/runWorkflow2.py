import requests
import json
import os
import argparse # Importar a biblioteca argparse

# --- Configurações ---
COMFYUI_API_URL = "http://127.0.0.1:8188/prompt"  # URL da API do ComfyUI
DEFAULT_WORKFLOW_FILE = "Basic Face Swap API.json"                   # Nome padrão do seu arquivo JSON do workflow

def find_node_by_class_type(workflow_data, class_type):
    """Encontra o primeiro nó com um dado class_type."""
    for node_id, node_info in workflow_data.items():
        if isinstance(node_info, dict) and node_info.get('class_type') == class_type:
            return node_id, node_info
    return None, None

def send_workflow_to_comfyui(workflow_json_path, output_filename_prefix):
    """
    Carrega um workflow JSON, modifica o prefixo do arquivo de saída,
    e o envia para a API do ComfyUI.
    """
    if not os.path.exists(workflow_json_path):
        print(f"Erro: O arquivo de workflow '{workflow_json_path}' não foi encontrado.")
        print("Certifique-se de que o arquivo JSON do workflow está na mesma pasta do script")
        print("ou forneça o caminho completo para ele.")
        return

    try:
        with open(workflow_json_path, 'r') as f:
            workflow_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{workflow_json_path}' não é um JSON válido.")
        print("Certifique-se de que você salvou o workflow no ComfyUI usando 'Save (API Format)'.")
        return
    except Exception as e:
        print(f"Erro ao carregar o arquivo de workflow: {e}")
        return

    # --- MODIFICAÇÃO: Alterar o prefixo do nome do arquivo no nó SaveImage ---
    save_image_id, save_image_data = find_node_by_class_type(workflow_data, "SaveImage")
    if save_image_data and 'inputs' in save_image_data and 'filename_prefix' in save_image_data['inputs']:
        # O ComfyUI irá adicionar o resto (timestamp, seed, etc.)
        save_image_data['inputs']['filename_prefix'] = output_filename_prefix
        print(f"Prefixo do arquivo de saída atualizado para: '{output_filename_prefix}'")
    else:
        print("Aviso: Nó SaveImage não encontrado ou sem campo 'filename_prefix' no workflow. A imagem pode não ser salva como esperado.")

    headers = {'Content-Type': 'application/json'}
    payload = {'prompt': workflow_data}

    print(f"\nEnviando workflow para o ComfyUI em {COMFYUI_API_URL}...")

    try:
        response = requests.post(COMFYUI_API_URL, json=payload, headers=headers)
        response.raise_for_status()

        print("Workflow enviado com sucesso!")
        response_json = response.json()
        if 'prompt_id' in response_json:
            print(f"ID do Prompt: {response_json['prompt_id']}")
        if 'node_errors' in response_json and response_json['node_errors']:
            print("Aviso: O ComfyUI retornou erros em nós:")
            for node_id, errors in response_json['node_errors'].items():
                print(f"  Nó {node_id}: {errors}")

    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão: Não foi possível conectar ao servidor ComfyUI em {COMFYUI_API_URL}.")
        print("Por favor, verifique se o ComfyUI está rodando e acessível.")
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        print(f"Resposta do servidor: {response.text}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Executa um workflow do ComfyUI via API, definindo um nome de arquivo de saída personalizado."
    )
    parser.add_argument(
        "output_name",
        type=str,
        help="O nome (prefixo) pelo qual o arquivo de imagem resultante deve ser salvo no diretório ./output do ComfyUI."
    )
    parser.add_argument(
        "--workflow_file",
        type=str,
        default=DEFAULT_WORKFLOW_FILE,
        help=f"Caminho para o arquivo JSON do workflow do ComfyUI (padrão: {DEFAULT_WORKFLOW_FILE})."
    )

    args = parser.parse_args()

    send_workflow_to_comfyui(args.workflow_file, args.output_name)
