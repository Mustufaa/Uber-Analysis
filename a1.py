from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# User input is directly passed to subprocess.getoutput without validation.
# User input is directly used to open files without any restrictions.
# User input is directly passed to eval() without any validation.
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# User input is directly passed to pickle.loads without validation.
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# Can lead to arbitrary code execution through untrusted data.
# Potential for arbitrary command execution.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Potential for arbitrary command execution.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Can lead to arbitrary code execution through untrusted data.
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# Allows execution of arbitrary Python code.
# Can lead to arbitrary code execution through untrusted data.
@app.route("/runcmd", methods=["POST"])
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
