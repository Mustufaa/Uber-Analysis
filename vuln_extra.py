import os
import json
import subprocess
import hashlib
from flask import Flask, request, abort
import pickle

app = Flask(__name__)

def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_system_cmd(cmd):
    return os.system(cmd)

def load_untrusted_json(data):
    return json.loads(data)

def run_subprocess_insecure(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode() + err.decode()

@app.route("/config", methods=["POST"])
def insecure_config():
    data = request.data
    return data

@app.route("/exec", methods=["POST"])
def insecure_exec():
    cmd = request.json.get("cmd")
    return os.popen(cmd).read()

@app.route("/upload", methods=["POST"])
def insecure_upload():
    f = request.files.get("file")
    filename = f.filename
    save_path = os.path.join("/tmp/uploads/", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    f.save(save_path)
    return "uploaded"

@app.route("/auth", methods=["POST"])
def insecure_auth():
    token = request.headers.get("Authorization")
    if token == "Bearer SUPER_SECRET_TOKEN_ABC123":
        return "ok"
    return ("forbidden", 403)

@app.route("/eval", methods=["POST"])
def insecure_eval():
    code = request.data.decode()
    return str(eval(code))

@app.route("/unpickle", methods=["POST"])
def insecure_unpickle():
    data = request.data
    return pickle.loads(data)

if __name__ == "__main__":
    app.run(port=5001)
