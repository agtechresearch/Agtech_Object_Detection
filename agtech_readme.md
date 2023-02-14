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
>
> **Image & Label structure**
> * train / val / test data split <br>
>  example: strFlower dataset <br>
> ![image](https://user-images.githubusercontent.com/74248395/218665696-bccca3c7-3c1e-4392-ab63-338fdc203901.png)

> **Create yaml file** <br>
> * create [filename].yaml <br>
> > path: [dataset root dir] <br>
> > train: [train images(relative)] <br>
> > val: [val images(relative)] <br>
> > test: [test images(relative)] #optional <br>
> > \#classes 
> > names: <br>
> >   0: Flower <br>
> >   1: Before_blooming <br>
> >   2: Receptacle <br>
> >   3: Green_small_fruit <br>
> >   4: Strawberry_1 <br>
> >   5: Strawberry_2 <br>
> >   6: Strawberry_3 <br>
> >   
> > \# If your dataset need to be downloaded <br>
> > \# you can also write Download script/URL (optional) <br>
> example: 7class_str.yaml <br> ![image](https://user-images.githubusercontent.com/74248395/218666223-27cc295a-12a4-44d4-a5c7-33491db0f57e.png)
>



 
