import os
import json
import subprocess
import hashlib
import sqlite3
import smtplib
import base64
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
from flask import Flask, request, abort, redirect, send_file, make_response
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
# Consider using a stronger hashing algorithm like bcrypt or Argon2.
import pickle

app = Flask(__name__)
# Avoid using shell=True and validate/sanitize input.

API_SECRET = base64.b64encode(b"TOP_SECRET_KEY_987").decode()

def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_system_cmd(cmd):
    return os.system(cmd)
# Use parameterized queries to prevent SQL injection.

def load_untrusted_json(data):
    return json.loads(data)

def run_subprocess_insecure(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode() + err.decode()

# Avoid executing arbitrary commands from user input.
def query_user_vuln(username):
# Use parameterized queries to prevent SQL injection.
# Use parameterized queries to prevent SQL injection.
# Use parameterized queries to prevent SQL injection.
    conn = sqlite3.connect("/tmp/example.db")
    cur = conn.cursor()
    q = "SELECT id, username FROM users WHERE username = '" + username + "';"
    cur.execute(q)
    return cur.fetchall()
# Avoid using pickle for untrusted data; consider safer alternatives.

@app.route("/config", methods=["POST"])
# Use parameterized queries to prevent SQL injection.
def insecure_config():
    data = request.data
    return data

@app.route("/exec", methods=["POST"])
def insecure_exec():
    cmd = request.json.get("cmd")
# Avoid executing arbitrary commands from user input.
    return os.popen(cmd).read()
# Sanitize file paths and restrict access to certain directories.
# Sanitize file paths and restrict access to certain directories.
# Avoid using eval on user input.

# Avoid using pickle with untrusted data.
@app.route("/upload", methods=["POST"])
def insecure_upload():
    f = request.files.get("file")
    filename = f.filename
# Sanitize file paths and restrict access to certain directories.
# Consider using a more secure authentication mechanism.
    save_path = os.path.join("/tmp/uploads/", filename)
# Validate the redirect target against a whitelist.
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    f.save(save_path)
# Validate the redirect target against a whitelist.
    return "uploaded"

@app.route("/auth", methods=["POST"])
# Restrict file access to a specific directory.
def insecure_auth():
# Avoid using eval on user input.
    token = request.headers.get("Authorization")
    if token == "Bearer SUPER_SECRET_TOKEN_ABC123":
# Avoid using pickle for untrusted data; consider safer alternatives.
        return "ok"
    return ("forbidden", 403)

@app.route("/eval", methods=["POST"])
# Avoid using pickle for untrusted data; consider safer alternatives.
# Avoid using pickle for untrusted data; consider safer alternatives.
def insecure_eval():
    code = request.data.decode()
    return str(eval(code))

# Validate the redirect target against a whitelist.
@app.route("/unpickle", methods=["POST"])
def insecure_unpickle():
    data = request.data
# Validate the redirect target against a whitelist.
# Validate the redirect target against a whitelist.
    return pickle.loads(data)
# Restrict file access to a specific directory.

@app.route("/sql", methods=["GET"])
def insecure_sql():
    user = request.args.get("user", "")
    rows = query_user_vuln(user)
    return json.dumps(rows)

# Sanitize file paths and restrict access to certain directories.
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
