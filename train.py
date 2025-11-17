from ultralytics import YOLO

model = YOLO("yolo11m.pt")

model.train(
    data='./data.yaml', 
    epochs=30,
    batch=16,
    imgsz=640,
    device='cuda:0',
    #device='cpu',
    name='yolo_v11x_V01',
    project='trained_models/yolo_v11_V01',
    save_period=5,
    amp=False,
    workers=0,
)

# Evaluate the model
metrics = model.val()

# Print validation metrics
print("Validation Results:")
for key, value in metrics.items():
    print(f"{key}: {value}")
