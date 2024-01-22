from flask import Flask, jsonify
import subprocess
import socket

app = Flask(__name__)

def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])

@app.route('/', methods=['POST'])
def run():
    stress_cpu()
    return "success"

@app.route('/', methods=['GET'])
def handle_get():
    private_ip = socket.gethostbyname(socket.gethostname())
    return str(private_ip)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)
