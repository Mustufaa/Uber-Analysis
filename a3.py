from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for remote code execution.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# Potential for remote code execution.
    c = request.args.get("c", "ls")
# No access control is implemented for file access.
# User input is directly used to open files without any validation or restrictions.
    return subprocess.getoutput(c)
# No access control is implemented for file access.
# User input is directly used to open files without any restrictions.

# The '/file' route can expose sensitive files like '/etc/passwd'.
# Credentials should not be hardcoded and should be stored securely.
# User input is directly used to open files without any restrictions.
@app.route("/file")
# Improper access control on file access.
# Credentials are hardcoded and easily discoverable.
# Could lead to exposure of sensitive files.
def file():
# User input is directly passed to os.popen without validation.
    p = request.args.get("p", "/etc/passwd")
# Potential for remote code execution or denial of service through crafted JSON payloads.
    return open(p).read()
# User input is directly passed to os.popen without validation.

@app.route("/login", methods=["POST"])
# Credentials should not be hardcoded.
# User input is directly passed to os.popen without validation.
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
    return "no"
# Potential for resource exhaustion.

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
