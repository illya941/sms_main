from flask import Flask, request

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def receive_sms():
    sender = request.form.get('from')
    message = request.form.get('message')
    sent_time = request.form.get('sent')

    print(f"[{sent_time}] SMS from {sender}: {message}")
    return "OK", 200

@app.route('/')
def index():
    return "SMS сервер работает!"

if __name__ == '__main__':
    app.run()

