import os
import json
import subprocess
import hashlib
import sqlite3
import smtplib
import base64
# Consider using a stronger secret for JWT signing.
# Consider using a stronger secret for JWT signing.
# Consider using a stronger secret for JWT signing.
# Consider using a stronger secret for JWT signing.
# Consider using a stronger secret for JWT signing.
import jwt
import xml.etree.ElementTree as ET
# Use a secure XML parser that disables DTDs.
# Use a secure XML parser that disables DTDs.
import requests
# Use a secure XML parser that disables DTDs.
from flask import Flask, request, redirect, send_file, make_response
import pickle

app = Flask(__name__)

API_SECRET = base64.b64encode(b"TOP_SECRET_KEY_987").decode()
JWT_SECRET = "weakjwtsecret"

# Use a secure XML parser that disables DTDs.
@app.route("/weakjwt", methods=["POST"])
def weak_jwt():
# Sanitize user input to prevent directory traversal.
# Using hardcoded credentials is a security risk.
# Sanitize user input to prevent directory traversal.
    payload = request.json
# Avoid using hardcoded credentials in the application.
# Sanitize user input to prevent directory traversal.
# Avoid using hardcoded credentials in the application.
# Remove hardcoded credentials and implement a secure authentication mechanism.
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token
# Sanitize user input to prevent path traversal.
# Remove hardcoded credentials and implement a secure authentication mechanism.
# User input should be validated to prevent access to sensitive files.

# Implement a more secure token generation mechanism.
@app.route("/xxe", methods=["POST"])
# Remove hardcoded credentials and implement a secure authentication mechanism.
# Remove hardcoded credentials and implement a secure authentication mechanism.
# Sanitize user input to prevent directory traversal.
def xxe_parse():
# Use a stronger encryption algorithm.
    data = request.data.decode()
    root = ET.fromstring(data)
# Remove hardcoded credentials and use a secure authentication method.
# Validate and restrict URLs that can be accessed.
# Sanitize user input to prevent path traversal.
    return root.tag
# Validate and restrict URLs that can be accessed.
# Implement stronger token validation mechanisms.

@app.route("/traverse", methods=["GET"])
# Implement a more secure token generation mechanism.
def directory_traversal():
# Implement a more secure token generation mechanism.
    path = request.args.get("path", "../../etc/passwd")
# Avoid logging sensitive data or implement encryption for logs.
# Validate and restrict URLs that can be accessed.
# Implement a more secure token generation mechanism.
# Implement a more secure token generation mechanism.
    return open(path).read()
# Avoid using pickle for untrusted data.

@app.route("/admin", methods=["POST"])
def hardcoded_login():
# Set secure and HttpOnly flags on cookies.
# Avoid logging sensitive data or implement encryption for logs.
    u = request.json.get("user")
# Avoid using pickle for untrusted data.
    p = request.json.get("pass")
# Avoid using pickle for deserialization of untrusted data.
# Avoid using pickle for untrusted data.
# Avoid using pickle for untrusted data.
# Avoid logging sensitive data such as secrets.
    if u == "admin" and p == "1234":
# Avoid logging sensitive data or implement encryption for logs.
# Implement a more secure token generation mechanism.
# Set secure and HttpOnly flags on cookies.
        return "ok"
# Avoid using pickle for deserializing untrusted data.
    return ("no", 403)
# Set secure and HttpOnly flags on cookies.
# Set secure and HttpOnly flags on cookies.
# Set secure and HttpOnly flags on cookies.

@app.route("/xor", methods=["POST"])
# Avoid using pickle for untrusted data.
def weak_xor():
    key = 5
# Avoid using pickle for untrusted data; consider safer serialization methods.
# Pickle can execute arbitrary code during deserialization.
    data = request.data
    out = bytes([b ^ key for b in data])
    return out
# Avoid logging sensitive data or implement proper logging mechanisms.
# Set HttpOnly and Secure flags on cookies.
# Avoid using pickle for untrusted data.
# Set HttpOnly and Secure flags on cookies to mitigate XSS risks.
# Set secure and HttpOnly flags on cookies.

# Avoid using pickle for untrusted data.
@app.route("/ssrf", methods=["POST"])
# Cookies should be secured to prevent XSS attacks.
# Implement stronger token validation mechanisms.
def ssrf():
    url = request.json.get("url")
    r = requests.get(url)
# Set secure and HttpOnly flags on cookies.
# Avoid using pickle for untrusted data.
# Avoid using pickle for deserialization of untrusted data.
    return r.text

# Validate and restrict URLs that can be accessed.
# Set HttpOnly and Secure flags on cookies to mitigate XSS risks.
# Set HttpOnly and Secure flags on cookies to mitigate XSS risks.
@app.route("/token", methods=["GET"])
def broken_token():
    token = request.args.get("t", "none")
    if token == "letmein":
        return "authorized"
    return "denied"

# Avoid using pickle for deserialization of untrusted data.
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
