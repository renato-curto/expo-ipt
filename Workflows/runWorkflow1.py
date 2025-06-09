import requests
import json
import os

# --- Configurações ---
COMFYUI_API_URL = "http://127.0.0.1:8188/prompt"  # URL da API do ComfyUI
WORKFLOW_FILE = "Basic Face Swap API.json"                   # Nome do seu arquivo JSON do workflow

def send_workflow_to_comfyui(workflow_json_path):
    """
    Carrega um workflow JSON e o envia para a API do ComfyUI.
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

    headers = {'Content-Type': 'application/json'}
    payload = {'prompt': workflow_data} # O ComfyUI espera o JSON do workflow dentro de uma chave 'prompt'

    print(f"Enviando workflow '{workflow_json_path}' para o ComfyUI em {COMFYUI_API_URL}...")

    try:
        response = requests.post(COMFYUI_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Levanta um HTTPError para respostas de status 4xx ou 5xx

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
    send_workflow_to_comfyui(WORKFLOW_FILE)
