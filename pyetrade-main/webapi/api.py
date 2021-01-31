import flask, pyetrade
from flask import Flask, request, jsonify
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

KVUri = f"https://brrkeys1.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Pyetrade API</h1><p>This site is a prototype API for pyetrade.</p>"

@app.route('/api/v1/test', methods=['GET'])
def api_accounts_list():
    retrievedSecret = client.get_secret('etradeSandboxKey')
    return retrievedSecret.value

app.run(host="0.0.0.0", port=int("5000"), debug=True)