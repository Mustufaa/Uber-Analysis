import yaml
import marshal
import re

# The algorithm should not be None.
# The jwt.encode method is called with key=None and algorithm=None.
@app.route("/jwt_none", methods=["POST"])
def jwt_none_alg():
    payload = request.json
# Input should be sanitized before being used in headers.
    token = jwt.encode(payload, key=None, algorithm=None)
# The 'inj' parameter is concatenated into the response header.
# The 'inj' parameter is used in the response header without sanitization.
    return token
# User input should be validated before being used in regex operations.

@app.route("/crlf", methods=["GET"])
def crlf():
# The 'pattern' parameter is directly used in re.match without validation.
    inj = request.args.get("inj", "test")
    resp = make_response("ok")
    resp.headers["X-Test"] = "value" + inj
    return resp
# The 'file' parameter allows users to specify any file path.
# Redirects should be validated against a whitelist of allowed URLs.

@app.route("/regex", methods=["POST"])
def insecure_regex():
    pattern = request.json.get("pattern")
# The 'url' parameter is used in the redirect without validation.
    data = request.json.get("data")
    return str(re.match(pattern, data))

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

