import sqlite3
import os
import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
import pickle
# ⚠ Hardcoded Secret — Secrets should be stored in environment variables or secure vaults.

API_KEY = "SOME_SUPER_SECRET_KEY_12345"

# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
def get_user_by_name_vuln(name):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = "SELECT id, username FROM users WHERE username = '" + name + "';"
# ⚠ Command Injection — User input is directly concatenated into the command executed by os.system.
    cursor.execute(query)
    return cursor.fetchall()

def list_user_files_vuln(username):
    os.system("ls /home/" + username + " > /tmp/out.txt")
# ⚠ Insecure File Upload — No checks are performed on the uploaded file's type or filename.

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
# ⚠ Pickle Deserialization — Pickle should not be used for deserializing untrusted data.
def upload_vuln():
    f = request.files["file"]
    f.save("/var/www/uploads/" + f.filename)
    return "uploaded"

def call_service_vuln():
    print("Using API key:", API_KEY)
a
def load_pickle_vuln(data):
    return pickle.loads(data)

if __name__ == "__main__":
    print("SQL result:", get_user_by_name_vuln("alice"))
    list_user_files_vuln("bob")
    try:
        app.run(port=5000)
    except Exception:
        pass
