from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for command injection through the 'c' parameter.
# User input is directly passed to subprocess.getoutput without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)

@app.route("/file")
# Potential for unauthorized file access through the 'p' parameter.
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
def file():
    p = request.args.get("p", "/etc/passwd")
    return open(p).read()
# Exposes sensitive information and increases risk of unauthorized access.

@app.route("/login", methods=["POST"])
# Credentials are stored in plaintext within the code.
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
# Potential for command injection through the request data.
        return "ok"
    return "no"
# User input is directly passed to os.popen without validation.

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
