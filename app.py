from flask import Flask
from flask_cors import CORS
from qr import qr_blueprint

app = Flask(__name__)
app.register_blueprint(qr_blueprint, url_prefix="/qr")
cors = CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.111', port=5000)