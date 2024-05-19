import cv2
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
#print(model.names) -> to get the Cars class ID 
results = model(source="/mnt/E/yolov8/homework1/argoverse.mp4", show=True, conf=0.4, save=True , classes=[2])