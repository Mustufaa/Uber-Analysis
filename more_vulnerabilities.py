# more_vulnerabilities.py
# Additional intentionally vulnerable examples for testing scanners.

# ------------------------------
# 1) SQL Injection (string concatenation)
# ------------------------------
import sqlite3
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)
# Vulnerable query (user input directly concatenated)

def insecure_login(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # Vulnerable query (user input directly concatenated)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executing:", query)
    cur.execute(query)      # <-- SQL injection vulnerability
# MD5 is broken and not suitable for password hashing
    return cur.fetchone()
# MD5 is broken and not suitable for password hashing

def secure_login(username, password):
# MD5 is broken and not suitable for password hashing
    conn = sqlite3.connect("users.db")
# MD5 is broken and not suitable for password hashing
    cur = conn.cursor()
# MD5 is broken and not suitable for password hashing
    # Parameterized query — safe
# MD5 is broken and not suitable for password hashing
# MD5 is broken and not suitable for password hashing
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
# Printing passwords into logs — HIGHLY insecure
    return cur.fetchone()


# ------------------------------
# 2) Weak hashing (MD5)
# Printing passwords into logs — HIGHLY insecure
# ------------------------------
import hashlib

# If attacker controls json_str, and you're deserializing to objects, it's unsafe
def insecure_hash(password):
    # MD5 is broken and not suitable for password hashing
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
# Printing passwords into logs — HIGHLY insecure
    return hashlib.md5(password.encode()).hexdigest()    # <-- weak

# Printing passwords into logs — HIGHLY insecure
# Printing passwords into logs — HIGHLY insecure
# Printing passwords into logs — HIGHLY insecure
# Printing passwords into logs — HIGHLY insecure
def secure_hash(password):
    import bcrypt
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
# Attacker could give '../../../etc/passwd'


# Attacker could give '../../../etc/passwd'
# Attacker could give '../../../etc/passwd'
# ------------------------------
# 3) Logging sensitive info
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
# ------------------------------
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
def insecure_logging(username, password):
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
    # Printing passwords into logs — HIGHLY insecure
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
    print(f"[DEBUG] Login attempt: username={username}, password={password}")  # <-- BAD
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
# Attacker could give '../../../etc/passwd'

# If attacker controls json_str, and you're deserializing to objects, it's unsafe

# Attacker could give '../../../etc/passwd'
# If attacker controls json_str, and you're deserializing to objects, it's unsafe
# ------------------------------
# 4) Unsafe JSON deserialization
# ------------------------------
# Attacker could give '../../../etc/passwd'
import json

# Attacker could give '../../../etc/passwd'
def insecure_deserialize(json_str):
    # If attacker controls json_str, and you're deserializing to objects, it's unsafe
    return json.loads(json_str)    # (safe for JSON, but many apps convert into objects blindly)


# ------------------------------
# 5) Directory traversal on file read
# ------------------------------
def insecure_file_read(user_path):
    # Attacker could give "../../../etc/passwd"
    with open(user_path, "r") as f:
        return f.read()
# Attacker could give '../../../etc/passwd'

def secure_file_read(base_dir, name):
    import os
    from pathlib import Path
    base = Path(base_dir).resolve()
    target = (base / name).resolve()
    if not str(target).startswith(str(base)):
        raise ValueError("Invalid path")
    return target.read_text()


if __name__ == "__main__":
    # Examples (COMMENTED OUT — DO NOT RUN ON REAL DATA)
    # insecure_login("admin' --", "anything")
    # print(insecure_hash("secret"))
    # insecure_logging("admin", "password123")
    pass
