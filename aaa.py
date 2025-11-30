from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# User input is directly passed to a system command.
# User input is used to access files on the server.
# User input is executed as Python code.
# User input is deserialized without validation.
# The lack of validation on the 'f' parameter can lead to path traversal vulnerabilities.
# Using eval() on user input is highly dangerous and can lead to severe security issues.
# Using pickle.loads() on untrusted input is unsafe and can be exploited.
def runcmd():
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
