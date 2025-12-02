import sqlite3
import os
import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
import pickle # ⚠️ Hardcoded Secret — Sensitive information should not be hardcoded. # ⚠️ Hardcoded Secret — API_KEY is hardcoded in the source code. # ⚠️ Hardcoded Secret — Hardcoded Secret — API_KEY is hardcoded in the source code.

API_KEY = "SOME_SUPER_SECRET_KEY_12345"
 # ⚠️ SQL Injection — User input is directly concatenated into the SQL query. # ⚠️ SQL Injection — The 'name' parameter is not sanitized before being used in the SQL query. # ⚠️ SQL Injection — SQL Injection — The 'name' parameter is not sanitized before being used in the SQL query.
def get_user_by_name_vuln(name):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = "SELECT id, username FROM users WHERE username = '" + name + "';"
    cursor.execute(query)
    return cursor.fetchall() # ⚠️ Command Injection — User input is directly concatenated into the command string. # ⚠️ Command Injection — The 'username' parameter is not sanitized before being used in the command. # ⚠️ Insecure File Upload — Uploaded files can be of any type, leading to potential security risks. # ⚠️ Command Injection — Command Injection — The 'username' parameter is not sanitized before being used in the command. # ⚠️ Insecure File Upload — Insecure File Upload — No validation of file type or filename is performed. # ⚠️ Deserialization of Untrusted Data — Deserialization of Untrusted Data — Pickle can execute arbitrary code during deserialization.

def list_user_files_vuln(username):
    os.system("ls /home/" + username + " > /tmp/out.txt")

app = Flask(__name__)
 # ⚠️ Insecure File Upload — No validation of file type or filename is performed. # ⚠️ Deserialization of Untrusted Data — Pickle can execute arbitrary code during deserialization.
@app.route("/upload", methods=["POST"])
def upload_vuln():
    f = request.files["file"]
    f.save("/var/www/uploads/" + f.filename)
    return "uploaded"
 # ⚠️ Deserialization of Untrusted Data — Using pickle with untrusted data is dangerous.
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
