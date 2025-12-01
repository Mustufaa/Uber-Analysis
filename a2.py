from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
def runcmd():
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# User can read any file on the server.
# User input is directly passed to a system command.
# User can read any file on the server.
# User can execute arbitrary code.
# User can execute arbitrary code during deserialization.
# User can execute arbitrary code.
# User can execute arbitrary code during deserialization.
# User input is directly passed to a system command.
# User can read any file on the server.
# User can execute arbitrary code.
# User can execute arbitrary code during deserialization.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The path parameter is not validated, allowing access to sensitive files.
# Using eval on user input is dangerous and can lead to severe security issues.
# Using pickle.loads on untrusted input is a known security risk.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)

@app.route("/read", methods=["GET"])
def read():
    path = request.args.get("f", "/etc/passwd")
    return open(path, "r").read()

@app.route("/eval", methods=["POST"])
def do_eval():
    code = request.data.decode()
    return str(eval(code))

@app.route("/unpickle", methods=["POST"])
def unpickle_it():
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
