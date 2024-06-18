from ultralytics import YOLO
import numpy as np

model= YOLO("yolov8m.pt")

source_image=r"D:\Coding_\Reflex_\Reflex_\assets\test_images\t1.png"
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

'''for r in result:
    # Iterate through each detected object
    for det in result:
        # det contains information about one detected object
        cls_id = det[5]  # The 6th element in det is the class id
        predicted_classes.append(cls_id)

# Print the predicted classes
print(predicted_classes)'''

'''boxes=result.boxes #boxes fro boundning box outputs
masks=result.masks # masks object for segmentation masks outputs
keypoints= result.keypoints # keypoints object for post outputs
probs= result.probs #probs object for classification outputs
obb= result.obb #orinted boxes for OBB outputs
result.show() #diplay to screen'''
