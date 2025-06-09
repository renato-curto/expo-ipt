# Expo IPT 2025

Generative AI for the Expo IPT 2025.

## Documentation

### Requirements

- Time and patience
- Lots of disk space (10GB+)
- NVIDIA graphics card
- Windows Pro
- Git

### Recomendations

- [Cygwin](https://www.cygwin.com/)
- [7-Zip](https://7-zip.org/)

### Installation

#### ComfyUI

Download `ComfyUI_windows_portable_nvidia.7z` from [GitHub](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z) and extract to `./expo-ipt/`.

Download `stable-diffusion-v1-5` from [Hugging Face](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

#### ComfyUI Manager

Go to `./expo-ipt/` and clone the repository:

```
git clone https://github.com/Comfy-Org/ComfyUI-Manager.git ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager/requirements.txt
```

Execute `./ComfyUI_windows_portable/run_nvidia_gpu.bat`, on the Windows Command Prompt to start ComfyUI to finish the installation. Test the system: load `/Workflow/Browse Templates/Image Generation` and click Run.

#### InsightFace

Verify your portable Python version:

```
./ComfyUI_windows_portable/python_embeded/python.exe --version
```

Download [InsightFace](https://github.com/Gourieff/Assets/tree/main/Insightface/) accordingly to your Python version. Example: for Python 3.12.10, download `insightface-0.7.3-cp312-cp312-win_amd64.whl` into `./expo-ipt/ComfyUI_windows_portable/`.

Install:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install ./ComfyUI_windows_portable/insightface-0.7.3-cp312-cp312-win_amd64.whl onnxruntime
```

#### ReActor

```
mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/ultralytics/bbox
```

Download `face_yolov8m.pt` Ultralytics model from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/blob/main/models/detection/bbox/face_yolov8m.pt) and place it into the above directory.

```
mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/sams
```

Download both Sams models from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/tree/main/models/sams) and place them into the above directory.

Clone the repository:

```
git clone https://codeberg.org/Gourieff/comfyui-reactor-node ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node
```

Execute ´./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node/install.bat´, on the Windows Command Prompt to finish the installation and then `./ComfyUI_windows_portable/run_nvidia_gpu.bat` to load the final working system.

#### rgthree-comfy

Close ComfyUI, stop server and clone the repository:

```
git clone https://github.com/rgthree/rgthree-comfy.git ComfyUI_windows_portable/ComfyUI/custom_nodes/rgthree-comfy
```

## Operation

## Operation

## References and useful links

[Como Instalar o InsightFace no ComfyUI](https://www.youtube.com/watch?v=qSGAQWxSMJw)<br>
[Como Fazer Troca de Rosto no ComfyUI com o ReActor](https://www.youtube.com/watch?v=lSuhpN5PM6c)<br>
[New AI Face Swap with ReActor and ComfyUI: How to Install and Use](https://www.youtube.com/watch?v=cFrDYl1FJwc)<br>
<br>
[ComfyUI](https://github.com/comfyanonymous/ComfyUI)<br>
[ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)<br>
[ReActor](https://codeberg.org/Gourieff/comfyui-reactor-nod)<br>
<br>
[QR Code Photobooth in TouchDesigner](https://www.youtube.com/watch?v=t8tIc5b58qM)<br>
[QR Code Maker in TouchDesigner](https://derivative.ca/community-post/asset/qr-code-maker/65759)