import flask, pyetrade
from flask import Flask, request, jsonify
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from selenium import webdriver

KVUri = f"https://brrkeys1.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
consumer_key = client.get_secret('etradeSandboxKey').value
consumer_secret = client.get_secret('etradeSandboxSecret').value
etrade_username = client.get_secret('etradeUsername').value
etrade_password = client.get_secret('etradePassword').value

oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
tokenurl = oauth.get_request_token()

driver = webdriver.Chrome()
driver.get(tokenurl)
driver.find_element_by_xpath('//*[@id="user_orig"]').send_keys('saitcho666')
driver.find_element_by_xpath('//*[@id="log-on-form"]/div[2]/div[2]/div/input').send_keys('Xwingx12!!')
driver.find_element_by_xpath('//*[@id="logon_button"]').click()
driver.get(tokenurl)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/input[3]').click()
code = driver.find_element_by_xpath('/html/body/div[2]/div/div/input').getAttribute('value')
tokens = oauth.get_access_token(code)

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