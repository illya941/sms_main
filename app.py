import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask-сервер запущен и слушает PORT"

@app.route('/sms/device', methods=['POST'])
def receive_sms():
    sender = request.form.get('from')
    message = request.form.get('message')
    print(f"SMS от {sender}: {message}")
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ← Ключевая строка
    app.run(host='0.0.0.0', port=port)

