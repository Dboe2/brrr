import flask, pyetrade
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Pyetrade API</h1><p>This site is a prototype API for pyetrade.</p>"

@app.route('/api/v1/accounts/list', methods=['GET'])
def api_accounts_list():
    return 'List sample'

app.run(host="0.0.0.0", port=int("5000"), debug=True)