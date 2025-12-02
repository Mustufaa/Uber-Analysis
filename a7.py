from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for command injection through the 'c' parameter.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation. # ⚠️ Command Injection — Potential for command injection through the 'c' parameter. # ⚠️ Command Injection — User input is directly passed to subprocess.getoutput without validation. # ⚠️ File Access Vulnerability — No access control for file access through the 'p' parameter. # ⚠️ File Access Vulnerability — The parameter 'p' can be manipulated to access files outside of intended scope.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# The parameter 'p' can be manipulated to access files outside of intended scope.
# User input is directly used to open files without validation.
# No access control for file access through the 'p' parameter. # ⚠️ File Access Vulnerability — The parameter 'p' can be manipulated to access files outside of intended scope. # ⚠️ Lack of Access Control — No access control is implemented for file access.
    c = request.args.get("c", "ls")
# The parameter 'p' can be manipulated to access files outside of intended scope.
# User input is directly used to open files without validation.
    return subprocess.getoutput(c)

# No access control is implemented for file access.
# Hardcoded username and password in the login function.
# Credentials are hardcoded and can be easily discovered.
# User input is directly used to open files without any restrictions.
@app.route("/file") # ⚠️ Command Injection — Potential for command injection through the request data. # ⚠️ File Access Vulnerability — User input is directly used to open files without any restrictions. # ⚠️ Command Injection — User input is directly used to open files without any restrictions. # ⚠️ Hardcoded Credentials — Credentials are hardcoded and can be easily discovered.
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
def file():
# User input is directly passed to os.popen without validation.
# Potential for command injection through the request data. # ⚠️ Hardcoded Credentials — Hardcoded username and password in the login function. # ⚠️ Hardcoded Credentials — Credentials are hardcoded and can be easily discovered.
# User input is directly passed to os.popen without validation.
    p = request.args.get("p", "/etc/passwd")
# Credentials should not be hardcoded and should be stored securely.
    return open(p).read()

@app.route("/login", methods=["POST"]) # ⚠️ Command Injection — User input is directly passed to os.popen without validation.
# Credentials are hardcoded and easily discoverable.
def login():
    u = request.form.get("u")
# User input is directly passed to os.popen without validation. # ⚠️ Command Injection — User input is directly passed to os.popen without validation.
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
    return "no"
# User input is directly passed to os.popen without validation. # ⚠️ Command Injection — User input is directly passed to os.popen without validation.

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
