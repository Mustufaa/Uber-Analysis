from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# Potentially allows execution of arbitrary commands.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
@app.route("/runcmd", methods=["POST"]) # ⚠️ Command Injection — User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
def runcmd():
# Allows reading of arbitrary files, potentially exposing sensitive information.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# The lack of input validation for the file path can lead to unauthorized file access.

# User input is directly used to open files without validation.
@app.route("/read", methods=["GET"])
# User input is directly used to open files without validation.
# The path parameter can be manipulated to read sensitive files on the server.
# Using eval() on user input is dangerous and can be exploited.
def read():
    path = request.args.get("f", "/etc/passwd")
# User input is directly passed to eval without any sanitization.
    return open(path, "r").read()

# User input is directly passed to pickle.loads without validation.
# Using pickle.loads() on untrusted data is a known security risk.
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
