from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)

# No access control or validation on the file path provided by the user.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# No access control is implemented for file access.
# User input is directly used to open files without validation.
def file():
    p = request.args.get("p", "/etc/passwd")
# Hardcoded credentials are insecure and should not be used in production.
    return open(p).read()

@app.route("/login", methods=["POST"])
# Credentials should not be hardcoded and should use secure storage mechanisms.
def login():
# User input is directly passed to json.loads without any checks.
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
    return "no"
# User input is directly passed to os.popen without validation.

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
