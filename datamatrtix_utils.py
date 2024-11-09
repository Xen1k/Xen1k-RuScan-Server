from pylibdmtx.pylibdmtx import decode
import cv2
import numpy as np
import base64
from image_utils import *
from code_types import *

def detect_and_mark_datamatrix(img_b64):
    img_path = "tests/mark.jpg"
    # Get the image that contains the QR code
    image = cv2.cvtColor(readb64(img_b64), cv2.COLOR_BGR2RGB)
    image_out = readb64(img_b64)
    # image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_RGB2GRAY)
    # image_out = cv2.imread(img_path)
    image = resize_cv2_image(image, 0.7)
    image_out = resize_cv2_image(image_out, 0.7)
    # image = cv2.medianBlur(image, 1)

    height, width = image.shape[:2]
    print(height)
    print(width)
    decoded_data = decode(image, max_count=10, threshold=50)
    
    for i in range(len(decoded_data)):
        rect = decoded_data[i].rect
        if(rect == None):
            continue
        points = []
        points.append([rect.left, height - rect.top])
        points.append([rect.left + rect.width, height - rect.top])
        points.append([rect.left + rect.width, height - rect.top - rect.height])
        points.append([rect.left, height - rect.top - rect.height])
        
        pts = np.array(points).astype(int)
        pts = pts.reshape((-1, 1, 2))

        print(points)
        # color, thickness and isClosed
        color = (0, 255, 0)
        if(decoded_data[i].data == None or len(decoded_data[i].data) == 0):
            color = (0, 0, 255)
        thickness = 3
        isClosed = True
        image_out = cv2.polylines(image_out, [pts], isClosed, color, thickness)

    # # Convert to base64
    retval, out_jpg_img = cv2.imencode('.jpg', image_out)
    out_img_b64 = base64.b64encode(out_jpg_img).decode('utf-8')

    decoded_entities = []
    for text in decoded_data:
        entity = DecodedEntity(str(text.data), CodeType.DATAMATRIX)
        decoded_entities.append(entity.to_dict())
    print(decoded_entities)
    
    # show_image_b64(out_img_b64)
    
    return out_img_b64, decoded_entities

# detect_and_mark_datamatrix('')
