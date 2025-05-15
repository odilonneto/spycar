from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        with open(os.path.join(UPLOAD_FOLDER, 'frame.jpg'), 'wb') as f:
            f.write(request.data)
        return 'OK', 200
    except Exception as e:
        return f'Erro: {e}', 500

@app.route('/frame.jpg')
def frame():
    return send_from_directory(UPLOAD_FOLDER, 'frame.jpg')

@app.route('/')
def index():
    return """<!doctype html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Live ESP32-CAM</title>
    <style>
      html, body {
        margin: 0;
        padding: 0;
        background: #000;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }
      img {
        display: block;
      }
    </style>
  </head>
  <body>
    <img id="cam" src="/frame.jpg" alt="frame">
    <script>
      const img = document.getElementById('cam');
      setInterval(() => {
        img.src = '/frame.jpg?_=' + new Date().getTime();
      }, 500);
    </script>
  </body>
</html>"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
