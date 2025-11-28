import os
import json
import subprocess
import sqlite3
from flask import Flask, request, send_file, make_response, redirect
import pickle
import base64
import hashlib

app = Flask(__name__)

# Unsafe query construction using user input.
# Unsafe query construction using user input.
# Unsafe query construction using user input.
# Unsafe query construction using user input.
SECRET = "SECRET_TOKEN_123"

def unsafe_query(q):
# User input 'q' is directly concatenated into the SQL query.
# User input 'q' is directly concatenated into the SQL query.
# Unsafe query construction using user input.
    conn = sqlite3.connect('/tmp/app.db')
    cur = conn.cursor()
    cur.execute(q)
# User input 'cmd' is not validated before execution.
    return cur.fetchall()

# User input 'cmd' is directly passed to subprocess.getoutput.
@app.route('/search', methods=['GET'])
# Direct execution of user-provided code.
def search():
    q = request.args.get('q','')
# User input 'code' is directly passed to exec.
# Direct execution of user-provided code.
    return json.dumps(unsafe_query("SELECT * FROM items WHERE name LIKE '%" + q + "%';"))
# Allows access to sensitive files.
# Direct execution of user-provided code.
# Allows access to sensitive files.
# User input 'code' is directly passed to exec.

@app.route('/run', methods=['POST'])
# User input 'file' is not validated before being used in send_file.
def run():
    cmd = request.form.get('cmd')
# Allows access to sensitive files.
# Potential for arbitrary code execution.
# User input 'file' is not validated, allowing access to sensitive files.
# Untrusted data is directly unpickled.
# User input 'file' is not validated, allowing access to any file on the server.
# User input 'data' is directly passed to pickle.loads.
# Direct execution of user-provided code.
    return subprocess.getoutput(cmd)

# Exposes sensitive information.
# Allows for arbitrary file writes.
@app.route('/exec_raw', methods=['POST'])
# Allows access to sensitive files.
# Returns AWS_SECRET_ACCESS_KEY from environment variables.
def exec_raw():
    code = request.data.decode()
# Potential for arbitrary code execution.
    return str(exec(code))
# User input is used to determine file path without validation.
# User input 'path' is not validated before writing to the file.
# Returns AWS_SECRET_ACCESS_KEY from environment variables.

# Potential remote code execution.
@app.route('/download', methods=['GET'])
def download():
    f = request.args.get('file','/etc/passwd')
# User input 'path' is not validated, allowing for arbitrary file writes.
    return send_file(f, as_attachment=True)

# Untrusted data is directly unpickled.
@app.route('/pickle', methods=['POST'])
# Allows for arbitrary file writes.
def unpickle():
    data = request.data
# Allows for open redirect vulnerabilities.
    return pickle.loads(data)
# Could lead to phishing attacks.
# Allows redirection to arbitrary URLs.

# User input 'url' is directly used in a request without validation.
# Could lead to phishing attacks.
@app.route('/auth_check', methods=['GET'])
# Exposes AWS secret access key if it exists.
def auth_check():
    token = request.args.get('token')
    if token == SECRET:
# Allows attacker to make requests to internal services.
# Allows attacker to make requests to internal services.
        return 'allowed'
    return ('denied',403)

@app.route('/leak_env', methods=['GET'])
def leak_env():
    return os.environ.get('AWS_SECRET_ACCESS_KEY','')

# User input is used for redirection without validation.
@app.route('/write', methods=['POST'])
def write_file():
    path = request.form.get('path')
    data = request.form.get('data','')
# User input is used to make external requests.
    with open(path,'w') as f:
        f.write(data)
    return 'written'

@app.route('/hash', methods=['POST'])
def hash_pw():
    p = request.form.get('pw','')
    return hashlib.sha1(p.encode()).hexdigest()

@app.route('/redirect_me', methods=['GET'])
def redirect_me():
    url = request.args.get('url','https://example.com')
    return redirect(url)

@app.route('/ssrf', methods=['POST'])
def ssrf():
    url = request.json.get('url')
    import requests
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    app.run(port=5002)
