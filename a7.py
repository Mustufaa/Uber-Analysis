from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for command injection through the 'c' parameter.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Access Control Vulnerability — User input is directly used to open files without any restrictions.
# User input is directly passed to subprocess.getoutput without validation.
# The parameter 'p' can be manipulated to access files outside of intended scope.
# ⚠ File Access Vulnerability — The parameter 'p' can be manipulated to access files outside of intended scope.
# User input is directly used to open files without validation.
# No access control for file access through the 'p' parameter.
    c = request.args.get("c", "ls")
# The parameter 'p' can be manipulated to access files outside of intended scope.
# User input is directly used to open files without validation.
    return subprocess.getoutput(c)

# No access control is implemented for file access.
# Hardcoded username and password in the login function.
# Credentials are hardcoded and can be easily discovered.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
def file():
# User input is directly passed to os.popen without validation.
# ⚠ File Access Vulnerability — No access control is implemented for file access.
# ⚠ Command Injection — Potential for command injection through the request data.
# Potential for command injection through the request data.
# User input is directly passed to os.popen without validation.
    p = request.args.get("p", "/etc/passwd")
# Credentials should not be hardcoded and should be stored securely.
# ⚠ File Access Vulnerability — No access control is implemented for file access.
# ⚠ Command Injection — Potential for command injection through the request data.
# ⚠ Command Injection — Potential for command injection through the request data.
# ⚠ Command Injection — Potential for command injection through the request data.
    return open(p).read()

# ⚠ Command Injection — User input is directly passed to os.popen without validation.
@app.route("/login", methods=["POST"])
# Credentials are hardcoded and easily discoverable.
def login():
# ⚠ File Access Vulnerability — User input is directly used to open files without any restrictions.
# ⚠ Command Injection — Potential for command injection through the request data.
    u = request.form.get("u")
# ⚠ Command Injection — User input is directly passed to os.popen without validation.
# User input is directly passed to os.popen without validation.
    p = request.form.get("p")
    if u == "admin" and p == "123":
# ⚠ Command Injection — User input is directly passed to os.popen without validation.
        return "ok"
    return "no"
# ⚠ Command Injection — User input is directly passed to os.popen without validation.
# User input is directly passed to os.popen without validation.

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
