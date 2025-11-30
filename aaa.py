from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The cmd parameter can be manipulated to execute arbitrary commands.
# The read function allows access to any file on the server.
# The do_eval function executes arbitrary Python code from user input.
# The unpickle_it function deserializes data from user input without validation.
# The cmd parameter can be manipulated to execute arbitrary commands.
# User input is directly passed to a system command.
# Path parameter can be manipulated to read arbitrary files.
# User input is executed as code.
# Untrusted data can lead to arbitrary code execution.
# User input is directly passed to a system command.
# Path parameter can be manipulated to read arbitrary files.
# User input is executed as code.
# Untrusted data can lead to arbitrary code execution.
# The read function allows access to any file on the server.
# The do_eval function executes arbitrary Python code from user input.
# The unpickle_it function deserializes data from user input without validation.
# The open(path, 'r') call can be exploited to read sensitive files on the server.
# Using eval() on user input is dangerous and can be exploited.
# Using pickle.loads() on untrusted data is a security risk.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The path parameter can be manipulated to read sensitive files on the server.
# Using eval() on user input is highly dangerous and can allow attackers to execute arbitrary code.
# Using pickle.loads() on untrusted data can allow attackers to execute arbitrary code.
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
