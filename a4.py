from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
def cmd():
# Potential for arbitrary command execution.
# User input is directly passed to subprocess.getoutput without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)

@app.route("/file")
# No access control is implemented for file access.
# No access control is implemented for file access.
# No access control is implemented for file access.
# No access control is implemented for file access.
# User input is directly used to open files without validation.
def file():
    p = request.args.get("p", "/etc/passwd")
    return open(p).read()
# Exposes sensitive information.
# Potential for arbitrary command execution.

@app.route("/login", methods=["POST"])
# Credentials should not be hardcoded in the source code.
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
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
