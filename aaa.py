from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# Potentially allows execution of arbitrary commands.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
@app.route("/runcmd", methods=["POST"])
# ⚠ Command Injection — User input is directly passed to subprocess.getoutput without validation.
# ⚠ Command Injection — User input is directly passed to subprocess.getoutput without validation.
# ⚠ Command Injection — User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
def runcmd():
# Allows reading of arbitrary files, potentially exposing sensitive information.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# The lack of input validation for the file path can lead to unauthorized file access.
# ⚠ Arbitrary File Read — The path parameter can be manipulated to read sensitive files on the server.

# ⚠ Arbitrary File Read — The path parameter can be manipulated to read sensitive files on the server.
# ⚠ Arbitrary File Read — The path parameter can be manipulated to read sensitive files on the server.
# User input is directly used to open files without validation.
# ⚠ Arbitrary File Read — The path parameter can be manipulated to read sensitive files on the server.
@app.route("/read", methods=["GET"])
# User input is directly used to open files without validation.
# The path parameter can be manipulated to read sensitive files on the server.
# Using eval() on user input is dangerous and can be exploited.
def read():
    path = request.args.get("f", "/etc/passwd")
# User input is directly passed to eval without any sanitization.
    return open(path, "r").read()
# ⚠ Code Injection — User input is directly passed to eval without any sanitization.

# ⚠ Code Injection — User input is directly passed to eval without any sanitization.
# User input is directly passed to pickle.loads without validation.
# ⚠ Code Injection — User input is directly passed to eval without any sanitization.
# ⚠ Code Injection — User input is directly passed to eval without any sanitization.
# Using pickle.loads() on untrusted data is a known security risk.
# User input is directly passed to eval without any sanitization.
# ⚠ Code Execution via Pickle — User input is directly passed to pickle.loads without validation.
# ⚠ Code Injection — User input is directly passed to pickle.loads without validation.
@app.route("/eval", methods=["POST"])
# Using eval() on user input is highly dangerous and can allow attackers to execute arbitrary code.
# ⚠ Code Execution via Pickle — User input is directly passed to pickle.loads without validation.
def do_eval():
# ⚠ Code Execution via Pickle — User input is directly passed to pickle.loads without validation.
    code = request.data.decode()
    return str(eval(code))
# User input is directly passed to pickle.loads without validation.
# ⚠ Code Execution via Pickle — User input is directly passed to pickle.loads without validation.

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
