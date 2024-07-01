import pyrebase
import os

config={
    "apiKey": "AIzaSyCapvaTuwCidEhJA6E-CDOH5DyOfiAfKUg",
    "authDomain": "uniduetraffic.firebaseapp.com",
    "projectId": "uniduetraffic",
    "storageBucket": "uniduetraffic.appspot.com",
    "messagingSenderId": "125639716972",
    "appId": "1:125639716972:web:8c683acf95558085fa2849",
    "measurementId": "G-64PB0776YR",
    "databaseURL":""
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

path_on_cloud_img="images/traffic_images" #path on cloud as specified
path_on_cloud_label="images/labels" #path on cloud as specified


local_path_img="assets/test_images/random_img/"
local_path_labels="assets/test/random_label/"
#list all files
files_and_dirs = os.listdir(local_path_img)
#join files to path
files_img = [f for f in files_and_dirs if os.path.isfile(os.path.join(local_path_img, f))]
files_label = [f for f in files_and_dirs if os.path.isfile(os.path.join(local_path_img, f))]
print(files_img)
#print(files)
paths_img=[]
paths_label=[]
# for i in range(1,len(files_img)+1):
#     print(i)
print(len(files_img))
for i in range(0,len(files_img)):
    paths_img.append(local_path_img+files_img[i])
    paths_label.append(local_path_labels+files_label[i])

print(len(paths_img))
for i in paths_img:
    storage.child(path_on_cloud_img).put(i)

for j in paths_img:
    storage.child(path_on_cloud_img).put(j)
