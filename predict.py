from ultralytics import YOLO
import sys

file = sys.argv[1]

model = YOLO('/home/Louis/TMAV_luftballons/trained_models/yolo_v12x_V01/yolo_v12x_V012/weights/best.pt')
#model.predict('./f11_png.rf.44650b188c2728c09f51c4fb49a83386.jpg', save=True, show=True);
model.predict(file, save=True, show=True);
