from qreader import QReader
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import base64
# from pylibdmtx.pylibdmtx import decode
# print(decode(cv2.imread('trash/mark.jpg')))
# Create a QReader instance
qreader = QReader()

def readb64(uri):
   nparr = np.fromstring(base64.b64decode(uri), np.uint8)
   return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

def detect_and_mark_qr(uri):
    img_path = "tests/1.jpg"
    # Get the image that contains the QR code
    image = cv2.cvtColor(readb64(uri), cv2.COLOR_BGR2RGB)
    image_out = readb64(uri)
    # cv2.imwrite("image.jpg", image)
    # image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    # image_out = cv2.imread(img_path)
    # resize
    # p = 0.5
    # w = int(image.shape[1] * p)
    # h = int(image.shape[0] * p)
    # image = cv2.resize(image, (w, h))
    # image_out = cv2.resize(image_out, (w, h))
    image = cv2.medianBlur(image, 1)

    # Adjusts the contrast by scaling the pixel values by 2.3 
    # brightness = 2
    # contrast = 2
    # image = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

    # Apply the sharpening kernel to the image using filter2D
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # image = cv2.filter2D(image, -1, kernel)

    decoded_text = qreader.detect_and_decode(image=image, return_detections=True)

    for text in decoded_text[0]:
        print(text)
        
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

    # cv2.namedWindow('edit.jpg', cv2.WINDOW_NORMAL)
    # cv2.imshow("edit.jpg", image_out)
    # cv2.imshow("edit.jpg", readb64(out_img_b64))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return out_img_b64, decoded_text[0]

# detect_and_mark_qr("") todo crash
