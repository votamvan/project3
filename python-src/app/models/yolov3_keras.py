import os
import subprocess
import cv2
import imutils
# internal import
from config import UPLOAD_FOLDER

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
yolo_weights = "shoes_all_yolov3_tiny_5000.weights"
yolo_data = "shoes_all.data"
yolo_config = "shoes_all_yolov3_tiny.cfg"


def create_yolov3_detect(filename):
    filename = UPLOAD_FOLDER + filename
    output_fname = "IMAGE_YOLOV3.png"

    command = f"cd {dir_path};"
    command = command + "${PWD}/darknet detector test " + f"{yolo_data} {yolo_config} {yolo_weights} '{filename}';"
    command = command + f"mv predictions.jpg {UPLOAD_FOLDER}{output_fname}"
    print(command)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = proc.stdout.read()
    print(output)
    return output_fname

