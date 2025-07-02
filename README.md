# Expo IPT 2025

Generative AI for the Expo IPT 2025.

## Documentation

### Requirements

- Time and patience
- Lots of disk space (100GB+)
- NVIDIA graphics card (12GB+)
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

To make ComfyUI accessible from other computers on your network, locate your machine's IP address (e.g., 192.168.15.13), choose an available port (e.g., 4090), and edit the file `./expo-ipt/ComfyUI_windows_portable/run_nvidia_gpu.bat`. Add the following arguments `--listen 192.168.15.13 --port 4090`, right after `ComfyUI\main.py`.

On the first run, you may need to grant the application access to the network or configure the Windows Firewall accordingly.

##### ComfyUI Manager

Go to `./expo-ipt/` and clone the repository:

```
git clone https://github.com/Comfy-Org/ComfyUI-Manager.git ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager/requirements.txt
```

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`. Test the system: load `/Workflow/Browse Templates/Image Generation` and click Run. On the 4090 it should take only 4.31 seconds.

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

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`.

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

To install all the requirements, using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node/` and double click `install.bat`.

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`.

To test, clck `/Workflow/Open`, select the `./expo-ipt/Workflows/Basic Face Swap.json` workflow (reload the images, if necessary) and execute it. The first run on the 4090 should take only 24.97 seconds. Subsequent runs, with a different source image, about 2.37 seconds.

#### Flux

##### Loras

Download the `flux1-canny-dev-lora.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

Download the `flux1-depth-dev-lora.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

Download the `diffusion_pytorch_model.safetensors` (FLUX.1-Turbo-Alpha) from [Hugging Face](https://huggingface.co/alimama-creative/FLUX.1-Turbo-Alpha/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/`.

##### Check points

Download the `flux1-dev-fp8.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

Download the `flux1-schnell-fp8.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/flux1-schnell/blob/main/flux1-schnell-fp8.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

Download the `512-inpainting-ema.safetensors` from [Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-2-inpainting/blob/main/512-inpainting-ema.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/`.

##### VAE

Download the `diffusion_pytorch_model.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main/vae)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/vae/`.

##### Redux

Download the `sigclip_vision_patch14_384.safetensors` from [Hugging Face](https://huggingface.co/Comfy-Org/sigclip_vision_384/blob/main/sigclip_vision_patch14_384.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/clip_vision/`.

Download the `flux1-redux-dev.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/style_models/`.

##### GGUF

Download the `flux1-dev-Q4_0.gguf` from [Hugging Face](https://huggingface.co/city96/FLUX.1-dev-gguf/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/unet/`.

Download the `flux1-schnell-Q4_0.gguf` from [Hugging Face](https://huggingface.co/city96/FLUX.1-schnell-gguf/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/unet/`.

Download the `t5xxl_fp8_e4m3fn.safetensors` and the `clip_l.safetensors` from [Hugging Face](https://huggingface.co/comfyanonymous/flux_text_encoders/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/clip/`.

Download the `ae.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/vae/`.

##### XLbas-AI ControlNet

Clone the repository:

```
git clone https://github.com/XLabs-AI/x-flux-comfyui.git ComfyUI_windows_portable/ComfyUI/custom_nodes/x-flux-comfyui
```

Go to `./expo-ipt/ComfyUI_windows_portable/ComfyUI/custom_nodes/x-flux-comfyui/` and run `../../../python_embeded\python.exe setup.py`.

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`.

Download the `flux-depth-controlnet-v3.safetensors` from [Hugging Face](https://huggingface.co/XLabs-AI/flux-controlnet-depth-v3/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/xlabs/controlnets/`.

Download the `flux-canny-controlnet-v3.safetensors` from [Hugging Face](https://huggingface.co/XLabs-AI/flux-controlnet-canny-v3/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/xlabs/controlnets/`.

##### [Run it Locally: Flux Upscale ControlNet + ComfyUI Workflow](https://www.youtube.com/watch?v=QOX6me13doM) by Olivio Sarikas

[Workflows & images](https://drive.google.com/file/d/1kM51XBuVYfq0RA_o5AtpnMXr6bdfEGNT/view)

Download the ` diffusion_pytorch_model.safetensors` from [Hugging Face](https://huggingface.co/jasperai/Flux.1-dev-Controlnet-Upscaler/tree/main) and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/controlnet/` as `Flux.1-dev-Controlnet-Upscaler.safetensors`.

Download the `flux1-dev-Q5_0.gguf` from [Hugging Face](https://huggingface.co/city96/FLUX.1-dev-gguf/tree/main) and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/unet/`.

Download the `Aesthetic_Amateur_Photo_V4_Beta_2.safetensors` from [Civitai](https://civitai.com/models/689192?modelVersionId=843103) and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/loras/` as `Flux_Aesthetic_Amateur_Photo_V4_Beta_2.safetensors`.

Download the `flux1-dev-Q5_0.gguf` from [Hugging Face](https://huggingface.co/city96/FLUX.1-dev-gguf/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/unet/`.

Download the ` t5xxl_fp16.safetensors` and the `clip_l.safetensors` from [Hugging Face](https://huggingface.co/comfyanonymous/flux_text_encoders/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/clip/`.

##### [Flux Inpainting in ComfyUI](https://www.youtube.com/watch?v=YNqacq9YuW8) by Jokerai

Download the ` flux1-fill-dev.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/unet/`.

##### [LTXV 0.9.7 Locally in ComfyUI with low VRAM](https://www.youtube.com/watch?v=KtqSm89n1zQ)

Clone the LTXVideo node repository:

```
git clone https://github.com/Lightricks/ComfyUI-LTXVideo.git ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-LTXVideo
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-LTXVideo/requirements.txt
```

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`.

Clone the VideoHelperSuite node repository:

```
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-VideoHelperSuite
```

Install the requirements:

```
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI-VideoHelperSuite/requirements.txt
```

To finish the installation, start ComfyUI. Using Windows Explorer, navigate to `./expo-ipt/ComfyUI_windows_portable/` double click `run_nvidia_gpu.bat`.

Clone the VideoHelperSuite node repository:

##### Flux.1-Kontext.dev

Download the [flux1-dev-kontext_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/diffusion_models/`.

Download the `ae.safetensors` from [Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/ae.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/vae/`.

Download the `clip_l.safetensors` from [Hugging Face](https://huggingface.co/comfyanonymous/flux_text_encoders/tree/main)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/clip/`.

Download the [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors)  and place it into `./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/text_encoders/`.

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
[Run it Locally: Flux Upscale ControlNet + ComfyUI Workflow](https://www.youtube.com/watch?v=QOX6me13doM)<br>
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