import sqlite3
import os
import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
import pickle
# ⚠ Exposure of Sensitive Information — Hardcoded API key in the source code.

API_KEY = "SOME_SUPER_SECRET_KEY_12345"
# ⚠ SQL Injection — User input should be parameterized to prevent SQL injection.
# ⚠ SQL Injection — User input is directly concatenated into the SQL query.

# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
def get_user_by_name_vuln(name):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = "SELECT id, username FROM users WHERE username = '" + name + "';"
# ⚠ Command Injection — User input is directly concatenated into the command string.
    cursor.execute(query)
    return cursor.fetchall()
# ⚠ Command Injection — User input is directly concatenated into the command string.

def list_user_files_vuln(username):
    os.system("ls /home/" + username + " > /tmp/out.txt")

app = Flask(__name__)
# ⚠ Insecure File Upload — No validation of file type or filename is performed.

@app.route("/upload", methods=["POST"])
def upload_vuln():
    f = request.files["file"]
    f.save("/var/www/uploads/" + f.filename)
    return "uploaded"
# ⚠ Deserialization of Untrusted Data — Using pickle with untrusted data is dangerous.
# ⚠ Deserialization of Untrusted Data — Using pickle to deserialize data without validation.

def call_service_vuln():
# ⚠ Deserialization of Untrusted Data — Avoid using pickle for deserializing untrusted data; consider safer alternatives.
    print("Using API key:", API_KEY)

def load_pickle_vuln(data):
    return pickle.loads(data)

if __name__ == "__main__":
    print("SQL result:", get_user_by_name_vuln("alice"))
    list_user_files_vuln("bob")
    try:
        app.run(port=5000)
    except Exception:
        pass
