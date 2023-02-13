# Quick start for agtech_lab


## YOLOv8
> ### 1. create **conda** virtual environment
> `conda create -n [environment name] python=[python version]` <br> 
> `pip install -r requirements.txt` <br>
> `conda activate [environment name]`

---
> ### 2-1. predict(inference)
> `cd YOLOv8` <br>
> `yolo detect predict model=[trained pt file path] source=[data path for inference] imgsz=[image size 640 or..] conf=[confidence threshold default=0.25] `

* example: `yolo detect predict source=[test_img_dir] model=./runs/detect/train11/weights/last.pt conf=0.25`
---
> ### 2-2. train
