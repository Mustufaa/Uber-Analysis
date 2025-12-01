from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

@app.route("/runcmd", methods=["POST"])
# User input is directly passed to subprocess.getoutput without validation.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
def runcmd():
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)

@app.route("/read", methods=["GET"])
# User input is directly used to open files without validation.
# The path parameter can be manipulated to read sensitive files on the server.
def read():
    path = request.args.get("f", "/etc/passwd")
    return open(path, "r").read()

# User input is directly passed to eval without any sanitization.
@app.route("/eval", methods=["POST"])
# Using eval() on user input is highly dangerous and can allow attackers to execute arbitrary code.
def do_eval():
    code = request.data.decode()
    return str(eval(code))
# User input is directly passed to pickle.loads without validation.

@app.route("/unpickle", methods=["POST"])
# Using pickle.loads() on untrusted data can allow attackers to execute arbitrary code.
def unpickle_it():
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
