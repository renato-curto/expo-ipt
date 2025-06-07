# Expo IPT 2025

Generative AI for the Expo IPT 2025.

## Documentation

### Requirements

- Patience
- Lots of disk space
- NVIDIA graphics card
- Windows Pro
- Git

### Recomendations

- [Cygwin](https://www.cygwin.com/)
- [7-Zip](https://7-zip.org/)

### Installation

#### ComfyUI

Download ComfyUI_windows_portable_nvidia.7z
extract to ./expo-ipt/

Download stable-diffusion-v1-5 from [Hugging Face](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors)
place it into ./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/checkpoints/

#### ComfyUI Manager

cd ./expo-ipt/
git clone https://github.com/Comfy-Org/ComfyUI-Manager.git ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager
./ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-manager/requirements.txt

? run ./expo-ipt/ComfyUI_windows_portable/run_nvidia_gpu.bat

#### InsightFace

verify your Python version with
./ComfyUI_windows_portable/python_embeded/python.exe --version

Download InsightFace from https://github.com/Gourieff/Assets/tree/main/Insightface/ according to your Python version
Example, for Python 3.12.10, download insightface-0.7.3-cp312-cp312-win_amd64.whl into ./expo-ipt/ComfyUI_windows_portable/

run ./ComfyUI_windows_portable/python_embeded/python.exe -m pip install ./ComfyUI_windows_portable/insightface-0.7.3-cp312-cp312-win_amd64.whl onnxruntime

#### ReActor

mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/ultralytics/bbox
Download the "face_yolov8m.pt" Ultralytics model from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/blob/main/models/detection/bbox/face_yolov8m.pt) and place it into the above directory

mkdir -p ./ComfyUI_windows_portable/ComfyUI/models/sams
Download both of "Sams" models from [Hugging Face](https://huggingface.co/datasets/Gourieff/ReActor/tree/main/models/sams) - download and put into the ./expo-ipt/ComfyUI_windows_portable/ComfyUI/models/sams directory

git clone https://codeberg.org/Gourieff/comfyui-reactor-node ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node
cd ./ComfyUI_windows_portable/ComfyUI/custom_nodes/comfyui-reactor-node/
run ./install.bat

## References and useful links

[Como Instalar o InsightFace no ComfyUI](https://www.youtube.com/watch?v=qSGAQWxSMJw)<br>
[Como Fazer Troca de Rosto no ComfyUI com o ReActor](https://www.youtube.com/watch?v=lSuhpN5PM6c)<br>
[New AI Face Swap with ReActor and ComfyUI: How to Install and Use](https://www.youtube.com/watch?v=cFrDYl1FJwc)<br>
<br>
[ComfyUI](https://github.com/comfyanonymous/ComfyUI)<br>
[ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)<br>
[ReActor](https://codeberg.org/Gourieff/comfyui-reactor-nod)