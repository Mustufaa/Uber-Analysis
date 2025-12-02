from flask import Flask, request
import os, subprocess, json

app = Flask(__name__)

@app.route("/cmd")
def cmd():
# Potential for remote code execution.
# Potential for remote code execution.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Remote Code Execution — Potential for remote code execution.
# ⚠ Remote Code Execution — Potential for remote code execution.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# ⚠ Improper Access Control — Could lead to exposure of sensitive files.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# ⚠ Improper Access Control — Could lead to exposure of sensitive files.
# ⚠ Sensitive Data Exposure — Could lead to exposure of sensitive files.
# ⚠ Access Control — Could lead to exposure of sensitive files.
# ⚠ Remote Code Execution — Potential for remote code execution.
# ⚠ Code Injection — Potential for remote code execution.
# ⚠ Remote Code Execution — Potential for remote code execution.
# ⚠ Code Injection — Potential for remote code execution.
# ⚠ Remote Code Execution — Potential for remote code execution.
# Potential for remote code execution.
# User input is directly passed to subprocess.getoutput without validation.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Sensitive Data Exposure — Could lead to exposure of sensitive files.
# ⚠ Sensitive Data Exposure — User input is directly used to open files without any restrictions.
# ⚠ Sensitive Data Exposure — Could lead to exposure of sensitive files.
# User input is directly passed to subprocess.getoutput without validation.
# ⚠ Improper Access Control — No access control is implemented for file access.
# Potential for remote code execution.
# ⚠ Improper Access Control — Could lead to exposure of sensitive files.
    c = request.args.get("c", "ls")
# No access control is implemented for file access.
# User input is directly used to open files without any validation or restrictions.
    return subprocess.getoutput(c)
# ⚠ Hardcoded Credentials — Credentials are hardcoded and easily discoverable.
# No access control is implemented for file access.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# ⚠ Resource Exhaustion — User input is directly passed to os.popen without validation.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# No access control is implemented for file access.
# No access control is implemented for file access.
# ⚠ Resource Exhaustion — User input is directly passed to os.popen without validation.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# User input is directly used to open files without any restrictions.
# User input is directly used to open files without any restrictions.

# Could lead to exposure of sensitive files.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# The '/file' route can expose sensitive files like '/etc/passwd'.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
# User input is directly used to open files without any restrictions.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Hardcoded Credentials — Credentials should not be hardcoded and should be stored securely.
@app.route("/file")
# Improper access control on file access.
# ⚠ Resource Exhaustion — Potential for resource exhaustion.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# Credentials should not be hardcoded and should be stored securely.
# Credentials are hardcoded and easily discoverable.
# ⚠ Resource Exhaustion — Potential for resource exhaustion.
# ⚠ Resource Exhaustion — Potential for resource exhaustion.
# Could lead to exposure of sensitive files.
# Potential for remote code execution or denial of service through crafted JSON payloads.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Remote Code Execution — Potential for remote code execution.
def file():
# User input is directly passed to os.popen without validation.
# ⚠ Remote Code Execution — Potential for remote code execution or denial of service through crafted JSON payloads.
# Potential for remote code execution or denial of service through crafted JSON payloads.
# Credentials should not be hardcoded and should be stored securely.
# ⚠ Remote Code Execution — Potential for remote code execution.
    p = request.args.get("p", "/etc/passwd")
# ⚠ Remote Code Execution — Potential for remote code execution.
# Potential for remote code execution or denial of service through crafted JSON payloads.
# User input is directly passed to os.popen without validation.
# ⚠ Resource Exhaustion — Potential for resource exhaustion.
# ⚠ Remote Code Execution — Potential for remote code execution.
    return open(p).read()
# ⚠ Remote Code Execution — Potential for remote code execution.
# Potential for resource exhaustion.
# User input is directly passed to os.popen without validation.

# ⚠ Resource Exhaustion — Potential for resource exhaustion.
# Potential for remote code execution or denial of service through crafted JSON payloads.
# ⚠ Remote Code Execution — Potential for remote code execution.
# Potential for remote code execution.
@app.route("/login", methods=["POST"])
# Potential for resource exhaustion.
# ⚠ Resource Exhaustion — User input is directly passed to os.popen without validation.
# ⚠ Remote Code Execution — Potential for remote code execution.
# Credentials should not be hardcoded.
# User input is directly passed to os.popen without validation.
def login():
    u = request.form.get("u")
# Potential for resource exhaustion.
    p = request.form.get("p")
# ⚠ Remote Code Execution — Potential for remote code execution.
    if u == "admin" and p == "123":
        return "ok"
# User input is directly passed to os.popen without validation.
# ⚠ Resource Exhaustion — User input is directly passed to os.popen without validation.
# ⚠ Remote Code Execution — Potential for remote code execution.
    return "no"
# User input is directly passed to os.popen without validation.
# Potential for resource exhaustion.

@app.route("/json", methods=["POST"])
def load_json():
# ⚠ Resource Exhaustion — Potential for resource exhaustion.
    return json.loads(request.data)

@app.route("/shell", methods=["POST"])
def shell():
    return os.popen(request.data.decode()).read()

if __name__ == "__main__":
    app.run(port=5004)
