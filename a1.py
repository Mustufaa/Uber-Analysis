from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# Potential for arbitrary command execution.
@app.route("/runcmd", methods=["POST"])
# User input is directly passed to subprocess.getoutput without validation.
def runcmd():
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# Potential for reading sensitive files.

@app.route("/read", methods=["GET"])
def read():
# User input is directly used to open files without validation.
    path = request.args.get("f", "/etc/passwd")
# Potential for arbitrary code execution.
    return open(path, "r").read()

@app.route("/eval", methods=["POST"])
def do_eval():
# User input is directly passed to eval without validation.
    code = request.data.decode()
    return str(eval(code))

@app.route("/unpickle", methods=["POST"])
def unpickle_it():
# User input is directly passed to pickle.loads without validation.
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
