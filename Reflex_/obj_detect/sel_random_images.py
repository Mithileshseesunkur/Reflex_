import random
import os
from PIL import Image
import shutil as sh


def sel_random_images(source_img, destination_img,
                      source_txt, destination_txt, num_images):
    
    if not os.path.exists(destination_img) and not os.path.exists(destination_txt):
        os.makedirs(destination_img)
        os.makedirs(destination_txt)

        #get a list of  all files in source folder
        all_files=os.listdir(source_img)

        #filter out images from source folder
        image_files =[f for f in all_files if f.lower().endswith(('.png','.jpeg','.jpg'))]

        #Select a random subset of image files
        selected_images = random.sample(image_files, min(num_images, len(image_files)))
        
        #copy selected images
        for img in selected_images:
            source_path_img=os.path.join(source_img,img)
            dest_path_img=os.path.join(destination_img, img)
            sh.copy2(source_path_img, dest_path_img)

             # Check for a corresponding text file and copy it if it exists
            text_file_name = os.path.splitext(img)[0] + '.txt'
            source_text_path = os.path.join(source_txt, text_file_name)
            if os.path.exists(source_text_path):
                dest_text_path = os.path.join(destination_txt, text_file_name)
                sh.copy2(source_text_path, dest_text_path)


        
    
    

source_img=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export\dataset\images"
destination_img=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export\random_img"

source_txt=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export\dataset\labels"
destination_txt=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export\random_label"
num_images=10

sel_random_images(source_img, destination_img,source_txt,destination_txt,num_images)


