from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for remote code execution.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)

@app.route("/file")
# Could lead to exposure of sensitive files.
def file():
    p = request.args.get("p", "/etc/passwd")
    return open(p).read()

@app.route("/login", methods=["POST"])
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
    return "no"

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
