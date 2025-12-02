from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for command injection attacks.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# Potential for command injection through the 'c' parameter.
# Potential for command injection attacks.
# ⚠ Command Injection — Potential for command injection through the 'c' parameter.
# ⚠ File Inclusion — No access control is implemented for file access.
# Potential for command injection attacks.
# ⚠ File Inclusion — No access control is implemented for file access.
# ⚠ Sensitive Information Exposure — Exposes sensitive information.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Sensitive Information Exposure — User input is directly used to open files without any restrictions.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ File Inclusion — No access control is implemented for file access.
# ⚠ File Inclusion — Allows access to arbitrary files on the server.
# ⚠ File Inclusion — No access control is implemented for file access.
# User input is directly passed to subprocess.getoutput without validation.
# Allows access to arbitrary files on the server.
    c = request.args.get("c", "ls")
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
# ⚠ Command Injection — Potential for command injection through the 'p' parameter.
    return subprocess.getoutput(c)
# No access control is implemented for file access.
# Potential for file inclusion attacks through the 'p' parameter.
# User input is directly used to open files without any validation or restrictions.
# Exposes sensitive information.
# Allows access to sensitive files on the server.

# ⚠ Command Injection — Potential for command injection through the 'p' parameter.
# Allows access to sensitive files on the server.
# No access control is implemented for file access.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# ⚠ Command Injection — Potential for command injection attacks.
# Credentials should not be hardcoded and should be stored securely.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# ⚠ Command Injection — Potential for command injection attacks.
# Potential for command injection attacks.
# ⚠ Command Injection — Potential for command injection attacks.
# No access control is implemented for file access.
# Credentials should not be hardcoded and should be stored securely.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Sensitive Information Exposure — User input is directly passed to os.popen without validation.
# User input is directly used to open files without validation.
# Exposes sensitive information.
def file():
# User input is directly passed to os.popen without validation.
# Potential for command injection attacks.
# Potential for command injection through the 'data' parameter.
# ⚠ Command Injection — Potential for command injection attacks.
# Exposes sensitive information.
# Potential for command injection attacks.
    p = request.args.get("p", "/etc/passwd")
# Credentials are stored in plaintext within the code.
# Could lead to unexpected behavior if malicious data is sent.
    return open(p).read()

# User input is directly passed to os.popen without validation.
# Potential for command injection attacks.
@app.route("/login", methods=["POST"])
# Potential for command injection attacks.
# ⚠ Command Injection — Potential for command injection attacks.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Command Injection — Potential for command injection attacks.
def login():
# User input is directly passed to os.popen without validation.
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
# Potential for command injection attacks.
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
