from ultralytics import YOLO
import numpy as np


def yolo_(image_path):
    model= YOLO("yolov8m.pt")    

    source_image=image_path #for current image being shown
    source_predicted=r"D:\Coding_\Reflex_\Reflex_\assets\test_images"
    result=model(source_image,show=True, 
                save=True,
                project=source_predicted,
                name='predicted',
                exist_ok=True,
                save_txt=True)

    predicted_classes = []

    for r in result:
        for c in r.boxes.cls:
            predicted=model.names[int(c)] 
            predicted_classes.append(predicted)



    predicted_classes = np.unique(predicted_classes)
    print(predicted_classes)
    return predicted_classes

