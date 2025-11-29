import os
import json
import subprocess
import hashlib
import sqlite3
import smtplib
import base64
from flask import Flask, request, abort, redirect, send_file, make_response
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
import pickle

app = Flask(__name__)

API_SECRET = base64.b64encode(b"TOP_SECRET_KEY_987").decode()

def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_system_cmd(cmd):
    return os.system(cmd)

def load_untrusted_json(data):
    return json.loads(data)

# Use parameterized queries to prevent SQL injection.
def run_subprocess_insecure(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Avoid executing commands directly from user input.
# Use parameterized queries to prevent SQL injection.
    out, err = proc.communicate()
    return out.decode() + err.decode()

def query_user_vuln(username):
    conn = sqlite3.connect("/tmp/example.db")
    cur = conn.cursor()
    q = "SELECT id, username FROM users WHERE username = '" + username + "';"
    cur.execute(q)
    return cur.fetchall()
# Use subprocess.run with a list of arguments instead of os.popen.
# Avoid using eval on user input.

# Implement file type and size validation.
@app.route("/config", methods=["POST"])
def insecure_config():
    data = request.data
    return data

# Validate the redirect target against a whitelist.
# Implement file type and size validation before saving uploaded files.
@app.route("/exec", methods=["POST"])
def insecure_exec():
    cmd = request.json.get("cmd")
    return os.popen(cmd).read()
# Avoid using eval() with untrusted input.

@app.route("/upload", methods=["POST"])
def insecure_upload():
    f = request.files.get("file")
    filename = f.filename
    save_path = os.path.join("/tmp/uploads/", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    f.save(save_path)
    return "uploaded"

@app.route("/auth", methods=["POST"])
# Validate the target URL against a whitelist of allowed domains.
def insecure_auth():
    token = request.headers.get("Authorization")
    if token == "Bearer SUPER_SECRET_TOKEN_ABC123":
        return "ok"
# Sanitize the filename input to prevent path traversal attacks.
    return ("forbidden", 403)

@app.route("/eval", methods=["POST"])
# Avoid using pickle for untrusted data; consider safer serialization formats.
def insecure_eval():
    code = request.data.decode()
    return str(eval(code))

@app.route("/unpickle", methods=["POST"])
def insecure_unpickle():
    data = request.data
    return pickle.loads(data)

@app.route("/sql", methods=["GET"])
def insecure_sql():
    user = request.args.get("user", "")
    rows = query_user_vuln(user)
    return json.dumps(rows)

@app.route("/redirect", methods=["GET"])
def insecure_redirect():
    target = request.args.get("to", "https://example.com")
    return redirect(target)

@app.route("/download", methods=["GET"])
def insecure_download():
    filename = request.args.get("file", "../../etc/passwd")
    return send_file(filename, as_attachment=True)

@app.route("/send", methods=["POST"])
def insecure_send_email():
    to = request.form.get("to")
    body = request.form.get("body", "")
    server = smtplib.SMTP("localhost")
    msg = f"Subject: Test\n\n{body}"
    server.sendmail("noreply@example.com", to, msg)
    server.quit()
    return "sent"

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["X-Api-Secret"] = API_SECRET
    return response

if __name__ == "__main__":
    app.run(port=5001)
