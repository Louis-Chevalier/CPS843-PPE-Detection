from ultralytics import YOLO
import sys

model_name ='yolo_v11x_V01'
model_type = "yolo11m.pt"

# python3 train.py model_name path/to/model_type
if len(sys.argv) == 3:
    model_type = sys.argv[2]
    model_name = sys.argv[1]
    print(f'Beginning training of {model_name} using {model_type}')
elif len(sys.argv) != 1 or len(sys.argv) !=3:
    print("Invalid amount of arguments")
    sys.exit()

model = YOLO(model_type)

model.train(
    data='./data.yaml', 
    epochs=15,
    batch=16,
    imgsz=640,
    device='cuda:0',
    #device='cpu',
    name=model_name,
    project='trained_models/'+model_name,
    save_period=5,
    amp=False,
    workers=0,
)

# Evaluate the model
metrics = model.val()
