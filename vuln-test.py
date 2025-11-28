import yaml
import marshal
import re

# The algorithm should not be None.
# The jwt.encode method is called with key=None and algorithm=None.
# The jwt.encode method is called with key=None and algorithm=None.
# The algorithm should not be None.
# The jwt.encode method is called with key=None and algorithm=None.
@app.route("/jwt_none", methods=["POST"])
# The 'inj' parameter is used in the response header without sanitization.
def jwt_none_alg():
# The 'inj' parameter is used in the response header without validation.
    payload = request.json
# Input should be validated before being used in regex.
# Input should be sanitized before being used in headers.
# The 'pattern' parameter is directly used in re.match without validation.
    token = jwt.encode(payload, key=None, algorithm=None)
# The 'inj' parameter is concatenated into the response header.
# File access should be restricted to prevent unauthorized access.
# The 'pattern' parameter is directly used in re.match without validation.
# The 'inj' parameter is used in the response header without sanitization.
# The 'file' parameter is used to read files without any restrictions.
    return token
# Redirects should be validated against a whitelist of allowed URLs.
# User input should be validated before being used in regex operations.

# The 'file' parameter is used to open files without any restrictions.
@app.route("/crlf", methods=["GET"])
# Authentication checks should be more robust.
def crlf():
# The 'pattern' parameter is directly used in re.match without validation.
    inj = request.args.get("inj", "test")
    resp = make_response("ok")
# Use safe loading methods like yaml.safe_load.
# The 'debug' parameter can be manipulated to bypass authentication.
    resp.headers["X-Test"] = "value" + inj
    return resp
# The 'file' parameter allows users to specify any file path.
# Redirects should be validated against a whitelist of allowed URLs.
# The application loads YAML data without validation.

@app.route("/regex", methods=["POST"])
def insecure_regex():
    pattern = request.json.get("pattern")
# Authentication checks should not rely on user-controlled input.
# The data is loaded from user input without any security measures.
# The 'url' parameter is used in the redirect without validation.
    data = request.json.get("data")
    return str(re.match(pattern, data))

# The blob is directly unmarshalled without validation.
# Use safe loading methods like yaml.safe_load for untrusted data.
@app.route("/bigread", methods=["GET"])
# The 'debug' parameter allows access to admin functionality.
# The data is loaded without any validation or sanitization.
def bigread():
    f = request.args.get("file", "/var/log/syslog")
    return open(f, "rb").read()

@app.route("/redir2", methods=["GET"])
def open_redirect2():
    target = request.args.get("url", "https://google.com")
    return redirect(target)

@app.route("/auth_bypass", methods=["GET"])
def auth_bypass():
    if request.args.get("debug") == "1":
        return "admin"
    return "user"

@app.route("/yaml", methods=["POST"])
def yaml_rce():
    data = request.data.decode()
    return str(yaml.load(data, Loader=yaml.FullLoader))

@app.route("/marshal", methods=["POST"])
def insecure_marshal():
    blob = request.data
    return marshal.loads(blob)

if __name__ == "__main__":
    app.run(port=5001)

