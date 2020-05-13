import os
import cv2
import imutils
# internal import
from config import UPLOAD_FOLDER
from .yolo3_one_file_to_detect_them_all import make_yolov3_model, WeightReader, preprocess_input
from .yolo3_one_file_to_detect_them_all import decode_netout, correct_yolo_boxes, do_nms, draw_boxes



dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
weights_path = dir_path + "yolov3.weights"
net_h, net_w = 416, 416
obj_thresh, nms_thresh = 0.5, 0.45
anchors = [[116,90,  156,198,  373,326],  [30,61, 62,45,  59,119], [10,13,  16,30,  33,23]]
labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", \
          "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", \
          "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", \
          "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", \
          "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", \
          "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", \
          "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", \
          "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", \
          "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", \
          "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

yolov3 = make_yolov3_model()
weight_reader = WeightReader(weights_path).load_weights(yolov3)

def create_yolov3_detect(filename):
    filename = UPLOAD_FOLDER + filename
    print(filename)
    # preprocess the image
    image = cv2.imread(filename)
    image_h, image_w, _ = image.shape
    new_image = preprocess_input(image, net_h, net_w)

    # run the prediction
    yolos = yolov3.predict(new_image)
    boxes = []
    for i in range(len(yolos)): # decode the output of the network
        boxes += decode_netout(yolos[i][0], anchors[i], obj_thresh, nms_thresh, net_h, net_w)

    # correct the sizes of the bounding boxes
    correct_yolo_boxes(boxes, image_h, image_w, net_h, net_w)

    # suppress non-maximal boxes
    do_nms(boxes, nms_thresh)

    # draw bounding boxes on the image using labels
    draw_boxes(image, boxes, labels, obj_thresh)

    output = imutils.resize(image, height=700)
    output_fname = "IMAGE_YOLOV3.png"
    cv2.imwrite(UPLOAD_FOLDER + output_fname, output)
    return output_fname

