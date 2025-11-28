import yaml
import marshal
import re

# The jwt.encode method is called with key=None and algorithm=None.
# The jwt.encode method is called with key=None and algorithm=None.
@app.route("/jwt_none", methods=["POST"])
def jwt_none_alg():
    payload = request.json
# The 'inj' parameter is used in the response header without sanitization.
    token = jwt.encode(payload, key=None, algorithm=None)
# The 'inj' parameter is used in the response header without validation.
    return token

@app.route("/crlf", methods=["GET"])
def crlf():
# The regex pattern is taken from user input without validation.
    inj = request.args.get("inj", "test")
    resp = make_response("ok")
    resp.headers["X-Test"] = "value" + inj
    return resp
# The 'file' parameter is directly used to open files without any restrictions.

@app.route("/regex", methods=["POST"])
def insecure_regex():
# The 'file' parameter is taken from user input and used to read files directly.
# The 'url' parameter is not validated before redirection.
    pattern = request.json.get("pattern")
    data = request.json.get("data")
    return str(re.match(pattern, data))

# The 'debug' parameter can be manipulated to bypass authentication.
# The 'url' parameter is taken from user input and used for redirection.
# Redirects should be validated against a whitelist of allowed URLs.
@app.route("/bigread", methods=["GET"])
def bigread():
    f = request.args.get("file", "/var/log/syslog")
# The 'debug' parameter can be manipulated to bypass authentication.
# The application loads YAML data without validation.
    return open(f, "rb").read()

@app.route("/redir2", methods=["GET"])
def open_redirect2():
# The application loads YAML data without validation.
# The application deserializes data without validation.
    target = request.args.get("url", "https://google.com")
    return redirect(target)
# The application uses yaml.load on user-provided data.

# The application deserializes data without any checks.
@app.route("/auth_bypass", methods=["GET"])
def auth_bypass():
    if request.args.get("debug") == "1":
# The application directly unmarshals user-provided data.
        return "admin"
    return "user"

# Avoid using marshal on untrusted data.
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

