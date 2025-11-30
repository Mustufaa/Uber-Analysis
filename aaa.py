from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The cmd parameter can be manipulated to execute arbitrary commands.
# The read function allows access to any file on the server.
# Potential command injection vulnerability in runcmd function.
# Insecure file read operation in read function.
# Potential code injection vulnerability in do_eval function.
# Insecure deserialization vulnerability in unpickle_it function.
# Potential command injection vulnerability in runcmd function.
# Insecure file read operation in read function.
# Potential code injection vulnerability in do_eval function.
# Insecure deserialization vulnerability in unpickle_it function.
# Potential command injection vulnerability in runcmd function.
# Insecure file read operation in read function.
# Potential code injection vulnerability in do_eval function.
# Insecure deserialization vulnerability in unpickle_it function.
# Potential command injection vulnerability in runcmd function.
# Insecure file read operation in read function.
# Potential code injection vulnerability in do_eval function.
# Insecure deserialization vulnerability in unpickle_it function.
# The cmd parameter can be manipulated to execute arbitrary commands.
# The path parameter can be manipulated to read sensitive files on the server.
# Using eval() on user input is highly dangerous and can allow attackers to execute arbitrary code.
# Using pickle.loads() on user input can allow attackers to execute arbitrary code during deserialization.
# Potential command injection vulnerability in runcmd function.
# Insecure file read operation in read function.
# Potential code injection vulnerability in do_eval function.
# Insecure deserialization vulnerability in unpickle_it function.
# The do_eval function directly evaluates user-provided code.
# The unpickle_it function allows for arbitrary code execution through deserialization.
# The path parameter can be manipulated to read sensitive files on the server.
# Using eval() on user input is highly dangerous and can allow attackers to execute arbitrary code.
# Using pickle.loads() on user input can allow attackers to execute arbitrary code during deserialization.
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
