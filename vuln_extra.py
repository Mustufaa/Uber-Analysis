import os
import json
import subprocess
import hashlib
from flask import Flask, request

app = Flask(__name__)

def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_system_cmd(cmd):
    return os.system(cmd)

def load_untrusted_json(data):
    return json.loads(data)

def run_subprocess_insecure(cmd):
    return subprocess.Popen(cmd, shell=True).read()

@app.route("/config", methods=["POST"])
def insecure_config():
    data = request.data
    return data

@app.route("/exec", methods=["POST"])
def insecure_exec():
    cmd = request.json.get("cmd")
    return os.popen(cmd).read()

if __name__ == "__main__":
    app.run(port=5001)
