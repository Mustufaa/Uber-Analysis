import os
import json
import subprocess
import sqlite3
from flask import Flask, request, send_file, make_response, redirect
import pickle
import base64
import hashlib

app = Flask(__name__)

SECRET = "SECRET_TOKEN_123"

def unsafe_query(q):
# User input 'q' is directly concatenated into the SQL query.
    conn = sqlite3.connect('/tmp/app.db')
    cur = conn.cursor()
    cur.execute(q)
    return cur.fetchall()

@app.route('/search', methods=['GET'])
# User input 'cmd' is directly passed to subprocess.getoutput.
def search():
    q = request.args.get('q','')
    return json.dumps(unsafe_query("SELECT * FROM items WHERE name LIKE '%" + q + "%';"))

# User input 'code' is directly passed to exec.
@app.route('/run', methods=['POST'])
def run():
    cmd = request.form.get('cmd')
    return subprocess.getoutput(cmd)
# User input 'file' is not validated, allowing access to sensitive files.

@app.route('/exec_raw', methods=['POST'])
def exec_raw():
    code = request.data.decode()
# User input 'data' is directly passed to pickle.loads.
    return str(exec(code))

@app.route('/download', methods=['GET'])
def download():
# Returns AWS_SECRET_ACCESS_KEY from the environment.
    f = request.args.get('file','/etc/passwd')
    return send_file(f, as_attachment=True)

@app.route('/pickle', methods=['POST'])
# User input 'path' is not validated.
def unpickle():
    data = request.data
    return pickle.loads(data)

# User input 'url' is not validated.
@app.route('/auth_check', methods=['GET'])
def auth_check():
    token = request.args.get('token')
    if token == SECRET:
        return 'allowed'
    return ('denied',403)

@app.route('/leak_env', methods=['GET'])
def leak_env():
    return os.environ.get('AWS_SECRET_ACCESS_KEY','')

@app.route('/write', methods=['POST'])
def write_file():
    path = request.form.get('path')
    data = request.form.get('data','')
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
