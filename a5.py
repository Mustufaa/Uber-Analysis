from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# User can specify any command.
# ⚠ Command Injection — User can specify any command.
# User input is directly passed to subprocess.getoutput without validation.
# User can specify any command.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User can specify any file path.
# User input is directly used to open files without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
# ⚠ Insecure Direct Object Reference — No access control is implemented for file access.
# User can specify any file path.
# Credentials are hardcoded and not securely stored.
# User can specify any file path.

# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# No access control is implemented for file access.
# Credentials are hardcoded and not stored securely.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded in the source code.
# User input is directly used to open files without any restrictions.
# Credentials should not be hardcoded in the source code.
# User input is directly passed to os.popen without validation.
def file():
# Credentials should not be hardcoded in the source code.
    p = request.args.get("p", "/etc/passwd")
# Credentials should not be hardcoded in the source code.
    return open(p).read()

# User input is directly passed to os.popen without validation.
# ⚠ Command Injection — User can execute arbitrary commands.
# User can execute arbitrary commands.
# User can execute arbitrary commands.
# User input is directly passed to os.popen without validation.
@app.route("/login", methods=["POST"])
# Credentials should not be hardcoded and should be stored securely.
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# User can execute arbitrary commands.
        return "ok"
# User can execute arbitrary commands.
# User input is directly passed to os.popen without validation.
    return "no"

@app.route("/json", methods=["POST"])
def load_json():
# ⚠ Command Injection — User can execute arbitrary commands.
    return json.loads(request.data)
# ⚠ Command Injection — User can execute arbitrary commands.

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
