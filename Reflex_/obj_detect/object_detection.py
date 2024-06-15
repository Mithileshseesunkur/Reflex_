from ultralytics import YOLO

model=YOLO("yolov8n.yaml")

results=model.train(data=r"D:\Coding_\Reflex_\Reflex_\Reflex_\obj_detect\config.yaml", epochs=1,resume=True)



