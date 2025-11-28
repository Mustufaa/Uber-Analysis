import os
import json
import subprocess
import hashlib
import sqlite3
import smtplib
import base64
# Consider using a stronger secret for JWT signing.
import jwt
import xml.etree.ElementTree as ET
import requests
from flask import Flask, request, redirect, send_file, make_response
import pickle

app = Flask(__name__)

API_SECRET = base64.b64encode(b"TOP_SECRET_KEY_987").decode()
JWT_SECRET = "weakjwtsecret"

# Use a secure XML parser that disables DTDs.
@app.route("/weakjwt", methods=["POST"])
def weak_jwt():
    payload = request.json
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token
# Sanitize user input to prevent path traversal.

@app.route("/xxe", methods=["POST"])
def xxe_parse():
    data = request.data.decode()
    root = ET.fromstring(data)
# Remove hardcoded credentials and use a secure authentication method.
    return root.tag

@app.route("/traverse", methods=["GET"])
def directory_traversal():
    path = request.args.get("path", "../../etc/passwd")
    return open(path).read()

@app.route("/admin", methods=["POST"])
def hardcoded_login():
    u = request.json.get("user")
    p = request.json.get("pass")
    if u == "admin" and p == "1234":
        return "ok"
    return ("no", 403)

@app.route("/xor", methods=["POST"])
def weak_xor():
    key = 5
    data = request.data
    out = bytes([b ^ key for b in data])
    return out
# Avoid logging sensitive data or implement proper logging mechanisms.

@app.route("/ssrf", methods=["POST"])
def ssrf():
    url = request.json.get("url")
    r = requests.get(url)
    return r.text

# Set HttpOnly and Secure flags on cookies to mitigate XSS risks.
@app.route("/token", methods=["GET"])
def broken_token():
    token = request.args.get("t", "none")
    if token == "letmein":
        return "authorized"
    return "denied"

@app.route("/log", methods=["POST"])
def insecure_log():
    secret = request.json.get("secret")
    with open("/tmp/logs.txt", "a") as f:
        f.write(secret + "")
    return "logged"

@app.route("/cookie", methods=["GET"])
def cookie_issue():
    resp = make_response("cookie set")
    resp.set_cookie("role", "admin")
    return resp

@app.route("/pay", methods=["POST"])
def fake_payment():
    amount = request.json.get("amount")
    card = request.json.get("card")
    return f"charged {amount} using {card}"

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["X-Api-Secret"] = API_SECRET
    return response

@app.route("/pickle", methods=["POST"])
def insecure_pickle():
    data = request.data
    obj = pickle.loads(data)
    return f"Received object of type {type(obj)}"

if __name__ == "__main__":
    app.run(port=5001)
