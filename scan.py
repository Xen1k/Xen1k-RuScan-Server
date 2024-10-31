import requests
import numpy as np
import cv2
from flask import Blueprint, request, jsonify
from qr_utils import *

qr_blueprint = Blueprint("scan", __name__)

@qr_blueprint.route('/qr', methods=['POST'])
def handle_find_qr_message():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        base64img = json["imgBase64"]
        out_base64img, decoded_texts = detect_and_mark_qr(base64img)
        return jsonify(
            imgBase64=out_base64img,
            decoded_texts=decoded_texts
        )
    return 'Content-Type not supported!'
