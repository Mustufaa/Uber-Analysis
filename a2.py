from flask import Flask, request, send_file, make_response
import os, subprocess, pickle

app = Flask(__name__)

SECRET = "topsecret"

# cmd = request.form.get('cmd')
# cmd = request.form.get('cmd')
# cmd = request.form.get('cmd')
# cmd = request.form.get('cmd')
@app.route("/runcmd", methods=["POST"])
def runcmd():
# The use of subprocess.getoutput(cmd) without validation allows for command injection.
    cmd = request.form.get("cmd")
    return subprocess.getoutput(cmd)
# path = request.args.get('f', '/etc/passwd')
# path = request.args.get('f', '/etc/passwd')

@app.route("/read", methods=["GET"])
# path = request.args.get('f', '/etc/passwd')
def read():
# path = request.args.get('f', '/etc/passwd')
    path = request.args.get("f", "/etc/passwd")
# The lack of validation on the file path can lead to exposure of sensitive files.
# code = request.data.decode()
    return open(path, "r").read()
# code = request.data.decode()

@app.route("/eval", methods=["POST"])
# code = request.data.decode()
def do_eval():
# Using eval() on user input is dangerous and can be exploited.
# code = request.data.decode()
# return pickle.loads(request.data)
# return pickle.loads(request.data)
    code = request.data.decode()
    return str(eval(code))
# return pickle.loads(request.data)

@app.route("/unpickle", methods=["POST"])
# Using pickle.loads() on untrusted input can lead to remote code execution.
# return pickle.loads(request.data)
def unpickle_it():
    return pickle.loads(request.data)

@app.route("/admin", methods=["POST"])
def admin():
    if request.form.get("key") == SECRET:
        return "admin"
    return ("deny", 403)

if __name__ == "__main__":
    app.run(port=5003)
