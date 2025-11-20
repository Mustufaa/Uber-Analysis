# vulnerable_examples.py
# PURPOSE:
#   A set of intentionally vulnerable code snippets for testing scanners or training.
#   EACH SNIPPET IS LABELED and includes a short mitigation note.
#
# WARNING:
#   Run only in an isolated environment. Do not execute code that processes
#   untrusted network inputs on production machines.

# ----------------------
# 1) Unsafe eval() usage (RCE risk)
# ----------------------
def insecure_eval(user_text):
    """
    Demonstrates unsafe use of eval on untrusted input.
    DO NOT use this pattern in production.
    """
    # Example attacker-controlled payload could be: "__import__('os').system('echo pwned')"
    return eval(user_text)  # <-- dangerous

def secure_eval_example(user_text):
    """Safer approach: do not eval user input. For simple literals use ast.literal_eval"""
    import ast
    try:
        return ast.literal_eval(user_text)
    except Exception:
        raise ValueError("Input not a safe literal")


# ----------------------
# 2) pickle.load on untrusted input (RCE via pickle gadgets)
# ----------------------
def insecure_pickle_load(path):
    """Loads a pickle file without validation (DANGEROUS if attacker controls file)."""
    import pickle
    with open(path, "rb") as f:
        return pickle.load(f)   # <-- dangerous

def secure_load_json(path):
    """Use JSON instead of pickle for untrusted interchange"""
    import json
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------
# 3) subprocess with shell=True and unsanitized input (command injection)
# ----------------------
def insecure_subprocess(user_arg):
    """
    Demonstrates passing user-controlled data to a shell command.
    If user_arg includes shell meta-characters, this can execute arbitrary commands.
    """
    import subprocess
    cmd = f"ls {user_arg}"
    subprocess.run(cmd, shell=True)   # <-- dangerous

def secure_subprocess(user_arg):
    """Use list args and avoid shell=True"""
    import subprocess
    subprocess.run(["ls", user_arg])  # safer (still validate user_arg)


# ----------------------
# 4) disabling TLS verification (MITM risk)
# ----------------------
def insecure_requests(url):
    """Example of disabling HTTPS verification."""
    import requests
    return requests.get(url, verify=False)  # <-- dangerous (man-in-the-middle risk)

def secure_requests(url):
    """Verify TLS; if using private CA, point to CA bundle."""
    import requests
    return requests.get(url)  # default is verify=True


# ----------------------
# 5) yaml.full_load (can construct arbitrary objects)
# ----------------------
def insecure_yaml_load(yaml_text):
    import yaml
    return yaml.full_load(yaml_text)  # <-- dangerous for untrusted YAML

def secure_yaml_load(yaml_text):
    import yaml
    return yaml.safe_load(yaml_text)


# ----------------------
# 6) Hard-coded secret (credential leak risk)
# ----------------------
API_KEY = "AKIA_EXAMPLE_very_secret_key_12345678"  # <- intentionally bad for testing

def use_api_key():
    """Example access to a hard-coded key. Do NOT commit real keys to source control."""
    print("Using API key length:", len(API_KEY))


# ----------------------
# 7) Unsafe file write without path validation (Directory traversal)
# ----------------------
def insecure_write(user_path, data):
    """Writes to a path coming from user input without validation (possible traversal)."""
    with open(user_path, "w", encoding="utf-8") as f:
        f.write(data)

def secure_write(safe_dir, filename, data):
    """Sanitize and restrict writes to a known directory."""
    import os
    from pathlib import Path
    safe_dir = Path(safe_dir).resolve()
    target = (safe_dir / filename).resolve()
    if not str(target).startswith(str(safe_dir)):
        raise ValueError("Invalid filename")
    with open(target, "w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    # Demo calls — comment/uncomment to experiment in an isolated environment.
    # NOTE: All calls below are commented to prevent accidental execution.
    #
    # print(insecure_eval("2+2"))
    # print(secure_eval_example("'hello'"))
    # insecure_subprocess("$(echo hacked)")   # don't run
    # print(insecure_requests("https://example.com"))
    # print(insecure_yaml_load("!!python/object/apply:os.system ['echo hi']"))
    # use_api_key()
    pass
