from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
# The use of subprocess.getoutput(cmd) without validation or sanitization of cmd is a critical vulnerability.
# Potentially exposes sensitive files on the server.
# Can lead to exposure of sensitive files.
# Allows execution of arbitrary Python code.
# Can lead to arbitrary code execution.
# Allows attackers to execute arbitrary commands on the server.
# Potentially exposes sensitive files on the server.
# Allows execution of arbitrary Python code.
# Can lead to arbitrary code execution or other attacks.
# The lack of validation on the 'f' parameter allows attackers to read arbitrary files.
# Using eval() on user input is highly dangerous and can be exploited to execute arbitrary code.
# Using pickle.loads() on untrusted data is a serious security risk.
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
