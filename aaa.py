from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# User input is directly passed to a system command.
@app.route("/runcmd", methods=["POST"])
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
def runcmd():
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)

@app.route("/read", methods=["GET"])
# The path parameter can be manipulated to read sensitive files on the server.
def read():
    path = request.args.get("f", "/etc/passwd")
    return open(path, "r").read()

@app.route("/eval", methods=["POST"])
# Using eval() on user input is dangerous and can be exploited.
def do_eval():
    code = request.data.decode()
    return str(eval(code))

@app.route("/unpickle", methods=["POST"])
# Using pickle.loads() on untrusted data is a known security risk.
def unpickle_it():
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
