from qreader import QReader
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import base64
from image_utils import *
from code_types import *

qreader = QReader()

def detect_and_mark_qr(img_b64):
    img_path = "tests/1.jpg"
    # Get the image that contains the QR code
    image = cv2.cvtColor(readb64(img_b64), cv2.COLOR_BGR2RGB)
    image_out = readb64(img_b64)
    # image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    # image_out = cv2.imread(img_path)
    image = cv2.medianBlur(image, 1)

    decoded_text = qreader.detect_and_decode(image=image, return_detections=True)

    for i in range(len(decoded_text[1])):
        qr_params = decoded_text[1][i]
        if(qr_params == None):
            continue
        if "padded_quad_xy" in qr_params:
            points = np.array(qr_params["quad_xy"]).astype(int)
            points = points.reshape((-1, 1, 2))
            # color, thickness and isClosed
            color = (0, 255, 0)
            if(decoded_text[0][i] == None):
                color = (0, 0, 255)
            thickness = 3
            isClosed = True
            image_out = cv2.polylines(image_out, [points], isClosed, color, thickness)

    # Convert to base64
    retval, out_jpg_img = cv2.imencode('.jpg', image_out)
    out_img_b64 = base64.b64encode(out_jpg_img).decode('utf-8')

    decoded_entities = []
    for text in decoded_text[0]:
        decoded_entities.append(DecodedEntity(text, CodeType.QR))
    
    # show_image_b64(out_img_b64)
    
    return out_img_b64, decoded_entities

# detect_and_mark_qr("") 
