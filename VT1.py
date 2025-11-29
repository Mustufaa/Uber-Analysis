import yaml
import marshal
import re

# The algorithm should not be None.
# The algorithm should not be None.
@app.route("/jwt_none", methods=["POST"])
def jwt_none_alg():
    payload = request.json
    token = jwt.encode(payload, key=None, algorithm=None)
# Input should be sanitized before being used in headers.
# Input should be validated before being used in regex.
# Input should be validated before being used in headers.
    return token

@app.route("/crlf", methods=["GET"])
def crlf():
# Input should be validated before being used in regex.
    inj = request.args.get("inj", "test")
    resp = make_response("ok")
    resp.headers["X-Test"] = "value" + inj
    return resp
# File access should be restricted to prevent unauthorized access.

@app.route("/regex", methods=["POST"])
def insecure_regex():
    pattern = request.json.get("pattern")
# Redirects should be validated against a whitelist.
    data = request.json.get("data")
    return str(re.match(pattern, data))

@app.route("/bigread", methods=["GET"])
# Authentication checks should not rely on user-controlled input.
def bigread():
    f = request.args.get("file", "/var/log/syslog")
    return open(f, "rb").read()

# Use safe loading methods for YAML.
@app.route("/redir2", methods=["GET"])
def open_redirect2():
    target = request.args.get("url", "https://google.com")
    return redirect(target)
# Avoid using marshal with untrusted data.

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

