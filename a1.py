from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# Potential for arbitrary command execution.
@app.route("/runcmd", methods=["POST"])
# Potential for arbitrary command execution.
def runcmd():
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# User input is directly passed to subprocess.getoutput without validation.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# Potential for reading sensitive files on the server.

# Potential for reading sensitive files.
# Potential for reading sensitive files on the server.
# Potential for reading sensitive files.
# Potential for reading sensitive files on the server.
@app.route("/read", methods=["GET"])
def read():
    path = request.args.get("f", "/etc/passwd")
# Potential for arbitrary code execution.
# Potential for arbitrary code execution through untrusted data.
# User input is directly used to open files without validation.
    return open(path, "r").read()
# Potential for arbitrary code execution through untrusted data.
# Potential for arbitrary code execution.
# Potential for arbitrary code execution.

# Potential for arbitrary code execution through untrusted data.
@app.route("/eval", methods=["POST"])
def do_eval():
# Potential for arbitrary code execution.
    code = request.data.decode()
# Potential for arbitrary code execution through untrusted data.
    return str(eval(code))
# Potential for arbitrary code execution through untrusted data.
# User input is directly evaluated without any restrictions.

@app.route("/unpickle", methods=["POST"])
def unpickle_it():
    return pickle.loads(request.data)

# User input is directly passed to pickle.loads without validation.
@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
