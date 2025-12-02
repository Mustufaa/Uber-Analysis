import sqlite3
import os
import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
import pickle

API_KEY = "SOME_SUPER_SECRET_KEY_12345"

# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
# ⚠ SQL Injection — User input is directly concatenated into the SQL query.
def get_user_by_name_vuln(name):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = "SELECT id, username FROM users WHERE username = '" + name + "';"
    cursor.execute(query)
# ⚠ Command Injection — User input is directly concatenated into the command executed by os.system.
    return cursor.fetchall()

def list_user_files_vuln(username):
    os.system("ls /home/" + username + " > /tmp/out.txt")
# ⚠ Insecure File Upload — No checks are performed on the uploaded file's type or content.

# ⚠ Insecure File Upload — No validation or sanitization of uploaded files.
app = Flask(__name__)

# ⚠ Insecure File Upload — No checks are performed on the uploaded file's type or content.
# ⚠ Pickle Deserialization — Pickle should not be used for deserializing untrusted data.
# ⚠ Deserialization of Untrusted Data — Using pickle with untrusted data is dangerous.
@app.route("/upload", methods=["POST"])
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
