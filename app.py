from flask import Flask
from flask_cors import CORS
from scan import qr_blueprint

app = Flask(__name__)
app.register_blueprint(qr_blueprint, url_prefix="/scan")
cors = CORS(app)


@app.route('/', methods=['GET'])
def handle_find_qr_message():
    return 'RuScan server is up'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.111', port=5000)