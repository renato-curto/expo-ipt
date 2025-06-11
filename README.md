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

##### Interface

Download `ComfyUI_windows_portable_nvidia.7z` from [GitHub](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z) and extract to `./expo-ipt/`.

Download `stable-diffusion-v1-5` from [Hugging Face](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

##### ComfyUI Manager

Go to `./expo-ipt/` and clone the repository:

```
git clone https://github.com/Comfy-Org/ComfyUI-Manager.git ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager/requirements.txt
```

Execute `./ComfyUI_windows_portable/run_nvidia_gpu.bat`, on the Windows Command Prompt to start ComfyUI to finish the installation. Test the system: load `/Workflow/Browse Templates/Image Generation` and click Run.

##### rgthree-comfy

Close ComfyUI, stop server and clone the repository:

```
git clone https://github.com/rgthree/rgthree-comfy.git ComfyUI_windows_portable/ComfyUI/custom_nodes/rgthree-comfy
```

##### ControlNet Auxiliary Preprocessors

Clone the node repository:

```
git clone https://github.com/Fannovel16/comfyui_controlnet_aux/ ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui_controlnet_aux
```

##### Use Everywhere Nodes

Clone the node repository:

```
git clone https://github.com/chrisgoringe/cg-use-everywhere.git ComfyUI_windows_portable/ComfyUI/custom_nodes/cg-use-everywhere
```

##### ComfyUI-GGUF

Clone the node repository:

```
git clone https://github.com/city96/ComfyUI-GGUF ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-GGUF
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-GGUF/requirements.txt
```

##### XLabs-AI

Clone the node repository:

```
git clone https://github.com/XLabs-AI/x-flux-comfyui.git ComfyUI_windows_portable/ComfyUI/custom_nodes/x-flux-comfyui
```

#### ReActor

##### InsightFace

Verify your portable Python version:

```
./ComfyUI_windows_portable/python_embeded/python.exe --version
```

Download [InsightFace](https://github.com/Gourieff/Assets/tree/main/Insightface/) accordingly to your Python version. Example: for Python 3.12.10, download `insightface-0.7.3-cp312-cp312-win_amd64.whl` into `./expo-ipt/ComfyUI_windows_portable/`.

Install:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install ./ComfyUI_windows_portable/insightface-0.7.3-cp312-cp312-win_amd64.whl onnxruntime
```

##### Requisites

```
mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/ultralytics/bbox
```

Download `face_yolov8m.pt` Ultralytics model from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/blob/main/models/detection/bbox/face_yolov8m.pt) and place it into the above directory.

```
mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/sams
```

Download both Sams models from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/tree/main/models/sams) and place them into the above directory.

##### ReActor custom node

Clone the repository:

```
git clone https://codeberg.org/Gourieff/comfyui-reactor-node ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node
```

Execute `./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node/install.bat`, on the Windows Command Prompt to finish the installation and then `./ComfyUI_windows_portable/run_nvidia_gpu.bat` to load the final working system.

#### Flux

##### Loras

Download the `flux1-canny-dev-lora.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

Download the `flux1-depth-dev-lora.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

Download the `diffusion_pytorch_model.safetensors` (
FLUX.1-Turbo-Alpha) from [Hugging Face](https://huggingface.co/alimama-creative/FLUX.1-Turbo-Alpha/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

##### Check points

Download the `flux1-dev-fp8.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

Download the `flux1-schnell-fp8.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/flux1-schnell/blob/main/flux1-schnell-fp8.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

##### VAE

Download the `diffusion_pytorch_model.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main/vae)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/vae/`.

##### Redux

Download the `sigclip_vision_patch14_384.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/sigclip_vision_384/blob/main/sigclip_vision_patch14_384.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/clip_vision/`.

Download the `lux1-redux-dev.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/style_models/`.

##### XLbas-AI ControlNet

Download the `flux-controlnet-depth-v3` from [Hugging Face](https://huggingface.co/XLabs-AI/flux-controlnet-depth-v3/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/xlabs/`.

#### pyqrcode for TouchDesigner

cd "\Program Files\Derivative\TouchDesigner\bin"

python.exe -m pip install pyqrcode

## Operation

## References and useful links

[Como Instalar o InsightFace no ComfyUI](https://www.youtube.com/watch?v=qSGAQWxSMJw)<br>
[Como Fazer Troca de Rosto no ComfyUI com o ReActor](https://www.youtube.com/watch?v=lSuhpN5PM6c)<br>
[New AI Face Swap with ReActor and ComfyUI: How to Install and Use](https://www.youtube.com/watch?v=cFrDYl1FJwc)<br>
[FLUX Redux: Simplified Workfloe (Style Transfer)](https://www.youtube.com/watch?v=nO8O0q2NLEA)<br>
<br>
[ControlNet Depth + FLUX Redux, Easy Workflow for ComfyUI](https://www.youtube.com/watch?v=lbtQEtyvHps)<br>
[The Simplest Workflow for FLUX on ComfyUI](https://www.youtube.com/watch?v=TWSFej_S_bY)<br>
[FLUX - Use Everywhere (UE) Nodes on ComfyUI](https://www.youtube.com/watch?v=cLhEOgABWFE)<br>
[GGUF FLUX ComfyUI: Boosting Workflows with Quantized Models](https://www.youtube.com/watch?v=AzeZkosyqp4)<br>
[FLUX Controlnet Workflow for Comfyui GGUF models](https://www.youtube.com/watch?v=HP_ocMsMdyI)<br>
<br>
[ComfyUI](https://github.com/comfyanonymous/ComfyUI)<br>
[ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)<br>
[ReActor](https://codeberg.org/Gourieff/comfyui-reactor-nod)<br>
<br>
[QR Code Photobooth in TouchDesigner](https://www.youtube.com/watch?v=t8tIc5b58qM)<br>
[QR Code Maker in TouchDesigner](https://derivative.ca/community-post/asset/qr-code-maker/65759)<br>
<br>
[TouchDesigner & ComfyUI: Magic AI Photobooth](https://www.youtube.com/watch?v=wc7UNt2BcVU)<br>
[ComfyTD Deep Dive](https://www.youtube.com/watch?v=jIIqE8cp420)<br>
<br>
[ComfyUI Flux Examples](https://comfyanonymous.github.io/ComfyUI_examples/flux/)<br>
[XLabs-AI FLUX ControlNet Collections](https://huggingface.co/XLabs-AI/flux-controlnet-depth-v3)
<br>
[PHP for Windows](https://windows.php.net/download/)