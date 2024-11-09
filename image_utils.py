import cv2
import numpy as np
import base64

def readb64(uri):
   nparr = np.fromstring(base64.b64decode(uri), np.uint8)
   return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

def show_image(image):
    cv2.namedWindow('edit.jpg', cv2.WINDOW_NORMAL)
    cv2.imshow("edit.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_image_b64(image_b64):
    cv2.namedWindow('edit.jpg', cv2.WINDOW_NORMAL)
    cv2.imshow("edit.jpg", readb64(image_b64))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_cv2_image(image, p):
    w = int(image.shape[1] * p)
    h = int(image.shape[0] * p)
    return cv2.resize(image, (w, h))

def sharpen_cv2_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def brighten_and_contrtast_cv2_image(image, brightness, contrast):
    return cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 