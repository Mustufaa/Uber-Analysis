from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# Potential for arbitrary command execution.
@app.route("/runcmd", methods=["POST"])
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
def runcmd():
# Potential for arbitrary command execution.
# User input is directly passed to subprocess.getoutput without validation.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# Potential for reading sensitive files.
# Potential for reading sensitive files.
# Potential for reading sensitive files.

# Potential for reading sensitive files.
@app.route("/read", methods=["GET"])
# Potential for reading sensitive files.
def read():
# Potential for reading sensitive files.
# Potential for reading sensitive files.
    path = request.args.get("f", "/etc/passwd")
# User input is directly used to open files without validation.
# Potential for arbitrary code execution through untrusted data.
# Potential for arbitrary code execution.
    return open(path, "r").read()
# Potential for arbitrary code execution through untrusted data.

@app.route("/eval", methods=["POST"])
# Potential for arbitrary code execution through untrusted data.
def do_eval():
    code = request.data.decode()
# Potential for arbitrary code execution through untrusted data.
# Potential for arbitrary code execution.
# Potential for arbitrary code execution.
# Potential for arbitrary code execution through untrusted data.
    return str(eval(code))
# Potential for arbitrary code execution through untrusted data.
# User input is directly passed to eval without validation.

@app.route("/unpickle", methods=["POST"])
# Potential for arbitrary code execution through untrusted data.
def unpickle_it():
    return pickle.loads(request.data)
# Potential for arbitrary code execution through untrusted data.
# Potential for arbitrary code execution through untrusted data.

# User input is directly passed to pickle.loads without validation.
@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
