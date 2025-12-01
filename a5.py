from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User can specify any file path.
# User input is directly used to open files without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
# Credentials are hardcoded and not securely stored.

# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# No access control is implemented for file access.
# Credentials are hardcoded and not stored securely.
# User input is directly used to open files without any restrictions.
# User input is directly passed to os.popen without validation.
def file():
    p = request.args.get("p", "/etc/passwd")
# Credentials should not be hardcoded in the source code.
    return open(p).read()

# User input is directly passed to os.popen without validation.
# User input is directly passed to os.popen without validation.
@app.route("/login", methods=["POST"])
# Credentials should not be hardcoded and should be stored securely.
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
# User input is directly passed to os.popen without validation.
    return "no"

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
