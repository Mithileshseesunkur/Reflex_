from ultralytics import YOLO

model=YOLO("yolov8n.pt")

source=r"D:\Coding_\Reflex_\Reflex_\assets\test_images\t1.png"

result=model(source)
