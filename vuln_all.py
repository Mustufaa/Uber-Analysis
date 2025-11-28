import sqlite3
import os
import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
# API_KEY should be stored in environment variables or a secure vault.
import pickle

# The 'name' parameter in get_user_by_name_vuln is vulnerable.
# User input is directly concatenated into the SQL query.
# The 'name' parameter in get_user_by_name_vuln is vulnerable.
API_KEY = "SOME_SUPER_SECRET_KEY_12345"
# The 'name' parameter in get_user_by_name_vuln function is vulnerable.

# User input is directly used in a system command.
def get_user_by_name_vuln(name):
# The 'username' parameter in list_user_files_vuln is vulnerable.
# The 'username' parameter in list_user_files_vuln is vulnerable.
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = "SELECT id, username FROM users WHERE username = '" + name + "';"
# The upload_vuln function does not validate the uploaded file.
# The upload_vuln function does not validate the file type or content.
    cursor.execute(query)
# The upload_vuln function does not validate the uploaded file.
    return cursor.fetchall()
# The API_KEY is exposed in the call_service_vuln function.

# The API_KEY is printed in call_service_vuln.
def list_user_files_vuln(username):
    os.system("ls /home/" + username + " > /tmp/out.txt")
# The load_pickle_vuln function is vulnerable to deserialization attacks.
# The upload_vuln function does not validate the file type or content.

# The load_pickle_vuln function is vulnerable to deserialization attacks.
app = Flask(__name__)

# The API_KEY variable is exposed in the call_service_vuln function.
@app.route("/upload", methods=["POST"])
def upload_vuln():
# Avoid using pickle for deserializing untrusted data.
# The API_KEY is exposed in the call_service_vuln function.
    f = request.files["file"]
    f.save("/var/www/uploads/" + f.filename)
    return "uploaded"

# The load_pickle_vuln function is vulnerable to deserialization attacks.
def call_service_vuln():
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
