import yaml
import marshal
import re

@app.route("/jwt_none", methods=["POST"])
def jwt_none_alg():
    payload = request.json
    token = jwt.encode(payload, key=None, algorithm=None)
    return token

@app.route("/crlf", methods=["GET"])
def crlf():
    inj = request.args.get("inj", "test")
    resp = make_response("ok")
    resp.headers["X-Test"] = "value" + inj
    return resp

@app.route("/regex", methods=["POST"])
def insecure_regex():
    pattern = request.json.get("pattern")
    data = request.json.get("data")
    return str(re.match(pattern, data))

@app.route("/bigread", methods=["GET"])
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

