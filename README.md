# Yolov8 
This a project about MVC Lab week 4 homework.
* In Homework 1, we use yolov8 pre-trained weight to do the object detection of 'car'.
*  In Homework 2, we download an dataset which is suitable for doing object detection task, and use the dataset to train 'yolov8n'.
  
## Homework1
Please setting your env first, and inference the yolov8 on Argoverse by 
```bash=
python object_detection.py
```
## Homework2
Please download the Aquarium Dataset first, and load pre-trained yolov8n for training.

####   Aquarium Dataset
link：https://public.roboflow.com/object-detection/aquarium
```
This dataset features 638 images from two US aquariums, labeled for object detection tasks. It includes various marine and aquatic species such as fish, jellyfish, penguins, sharks, puffins, stingrays, and starfish, with most images containing multiple bounding boxes. Released under a Creative Commons By-Attribution license, the dataset supports diverse applications from coral reef conservation to pet analytics. Formats provided are compatible with popular machine learning platforms, encouraging use in both personal and commercial projects.
```
After training and validating, the results show below :
| Class     | Images | Instances | Precision | Recall | mAP50 | mAP50-95 |
| --------- | ------ | --------- | --------- | ------ | ----- | -------- |
| All       | 127    | 909       | 0.824     | 0.688  | 0.767 | 0.469    |
| Fish      | 127    | 459       | 0.858     | 0.713  | 0.795 | 0.451    |
| Jellyfish | 127    | 155       | 0.843     | 0.858  | 0.915 | 0.529    |
| Penguin   | 127    | 104       | 0.687     | 0.654  | 0.702 | 0.322    |
| Puffin    | 127    | 74        | 0.714     | 0.608  | 0.640 | 0.324    |
| Shark     | 127    | 57        | 0.927     | 0.664  | 0.740 | 0.471    |
| Starfish  | 127    | 27        | 0.896     | 0.593  | 0.772 | 0.600    |
| Stingray  | 127    | 33        | 0.846     | 0.727  | 0.808 | 0.588    |

The values for each category indicate the model's detection capabilities for that type of object. Sharks and jellyfish exhibited relatively better performance, whereas penguins and puffins showed poorer results.

Moreover, I have applied the trained model to an unseen set.
![alt text](homework2/runs/detect/predict/IMG_2289_jpeg_jpg.rf.fe2a7a149e7b11f2313f5a7b30386e85.jpg)
![alt text](homework2/runs/detect/predict2/IMG_2371_jpeg_jpg.rf.54505f60b6706da151c164188c305849.jpg)
![alt text](homework2/runs/detect/predict3/IMG_2582_jpeg_jpg.rf.14f175066ce74b470bf31fa0c7a096cd.jpg)

More details are in  **homework2/object_detections.ipynb**

## Prerequisites
* ultralytics              8.2.18
* opencv-python            4.9.0.80
* torch                    2.3.0