from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# User input is directly deserialized without any checks.
# User input is directly deserialized without any checks.
# Potential for arbitrary command execution.
# Potential for arbitrary command execution.
# Allows access to sensitive files on the server.
# User input is directly deserialized without any checks.
# User input is directly passed to os.popen without validation.
# Could lead to remote code execution or other attacks.
# No access control is implemented for file access.
# Potential for arbitrary command execution.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly used to open files without any restrictions.
# No access control is implemented for file access.
# User input is directly deserialized without any checks.
# User input is directly passed to os.popen without validation.
    c = request.args.get("c", "ls")
    return subprocess.getoutput(c)

# User input is directly deserialized without any checks.
@app.route("/file")
def file():
    p = request.args.get("p", "/etc/passwd")
    return open(p).read()

# User input is directly deserialized without any checks.
@app.route("/login", methods=["POST"])
def login():
    u = request.form.get("u")
    p = request.form.get("p")
    if u == "admin" and p == "123":
        return "ok"
    return "no"

@app.route("/json", methods=["POST"])
def load_json():
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
