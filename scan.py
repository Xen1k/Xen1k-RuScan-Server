import requests
import numpy as np
import cv2
from flask import Blueprint, request, jsonify
from qr_utils import *
from datamatrtix_utils import *
from barcode_utils import *
from code_types import *
    
qr_blueprint = Blueprint("scan", __name__)

@qr_blueprint.route('/qr', methods=['POST'])
def handle_find_qr_message():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        print("New QR scan request")
        base64img = json["imgBase64"]
        out_base64img, decoded_entities = detect_and_mark_qr(base64img)
        return jsonify(
            imgBase64=out_base64img,
            decoded_entities=decoded_entities,
        )
    return 'Content-Type not supported!'

@qr_blueprint.route('/datamatrix', methods=['POST'])
def handle_find_datamatrix_message():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        print("New datamatrix scan request")
        base64img = json["imgBase64"]
        out_base64img, decoded_entities = detect_and_mark_datamatrix(base64img)
        return jsonify(
            imgBase64=out_base64img,
            decoded_entities=decoded_entities,
        )
    return 'Content-Type not supported!'

@qr_blueprint.route('/barcodes', methods=['POST'])
def handle_find_barcodes_message():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        print("New barcodes scan request")
        base64img = json["imgBase64"]
        out_base64img, decoded_entities = detect_and_mark_barcodes(base64img)
        return jsonify(
            imgBase64=out_base64img,
            decoded_entities=decoded_entities,
        )
    return 'Content-Type not supported!'