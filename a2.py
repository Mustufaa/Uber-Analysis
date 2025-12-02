from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The use of subprocess.getoutput(cmd) without validation allows for command injection. # ⚠️ Command Injection — The use of subprocess.getoutput(cmd) without validation allows for command injection. # ⚠️ Command Injection — ⚠️ Command Injection — The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
@app.route("/runcmd", methods=["POST"])
def runcmd():
# User input is directly passed to subprocess.getoutput without validation.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# The lack of validation on the file path can lead to exposure of sensitive files. # ⚠️ File Exposure — User input is used directly in file operations without any restrictions. # ⚠️ File Exposure — ⚠️ File Exposure — User input is used directly in file operations without any restrictions.

# The lack of validation on the file path can lead to exposure of sensitive files.
# User input is used directly in file operations without any restrictions.
# The lack of validation on the file path can lead to exposure of sensitive files.
@app.route("/read", methods=["GET"])
# The lack of validation on the file path can lead to exposure of sensitive files.
# The lack of validation on the file path can lead to exposure of sensitive files.
def read():
# The lack of validation on the file path can lead to exposure of sensitive files.
# Using eval() on user input is dangerous and can be exploited. # ⚠️ File Exposure — User input is directly passed to eval without any sanitization. # ⚠️ File Exposure — ⚠️ File Exposure — User input is directly passed to eval without any sanitization.
# Using eval() on user input is dangerous and can be exploited.
# User input is directly passed to eval without any sanitization.
    path = request.args.get("f", "/etc/passwd")
# The lack of input validation for the file path can lead to unauthorized file access.
# Using eval() on user input is dangerous and can be exploited.
# Using eval() on user input is dangerous and can be exploited.
    return open(path, "r").read()
# User input is directly passed to pickle.loads without validation.
# Using eval() on user input is dangerous and can be exploited.
# Using pickle.loads() on untrusted input can lead to remote code execution. # ⚠️ Remote Code Execution — User input is directly passed to eval without any sanitization.

@app.route("/eval", methods=["POST"])
# Using pickle.loads() on untrusted input can lead to remote code execution.
def do_eval():
# Using eval() on user input is dangerous and can be exploited.
# Using eval() on user input is dangerous and can be exploited.
# Using pickle.loads() on untrusted input can lead to remote code execution.
    code = request.data.decode()
    return str(eval(code))
 # ⚠️ Remote Code Execution — User input is directly passed to pickle.loads without validation.
# Using pickle.loads() on untrusted input can lead to remote code execution.
@app.route("/unpickle", methods=["POST"])
# Using pickle.loads() on untrusted input can lead to remote code execution.
# Using pickle.loads() on untrusted input can lead to remote code execution.
def unpickle_it():
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
