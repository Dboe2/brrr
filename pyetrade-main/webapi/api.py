import flask, pyetrade
from flask import Flask, request, jsonify
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

KVUri = f"https://brrkeys1.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
consumer_key = client.get_secret('etradeSandboxKey').value
consumer_secret = client.get_secret('etradeSandboxSecret').value

oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
tokenurl = oauth.get_request_token()

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Brrr API</h1><p>This site is a prototype API for pyetrade.</p>"

@app.route('/api/v1/accounts/list', methods=['GET'])
def api_accounts_list():
    accounts = pyetrade.ETradeAccounts(
        consumer_key,
        consumer_secret,
        tokens['oauth_token'],
        tokens['oauth_token_secret']
    )
    return print(accounts.list_accounts())

app.run(host="0.0.0.0", port=int("5000"), debug=True)