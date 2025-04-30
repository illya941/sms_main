import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask-сервер запущен и слушает PORT"

@app.route('/sms/device', methods=['POST'])
def receive_sms():
    #sender = request.form.get('from')
    #message = request.form.get('message')
    #print(f"SMS от {sender}: {message}")
    
    #print("=== RAW DATA ===")
    #print(request.data)
    #print("=== FORM ===")
    #print(request.form)
    #print("=== JSON ===")
    #print(request.get_json(silent=True))
    
    #data = request.get_json()
    #print(data)
    
    try:
        data = request.get_json()
        print("JSON:", data)
        message = data.get('message')
    except:
        message = request.form.get('message')
    
    print("MESSAGE:", message)
    
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ← Ключевая строка
    app.run(host='0.0.0.0', port=port)

