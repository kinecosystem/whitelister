import flask
import kin

app = flask.Flask(__name__)
env = kin.Environment('BLABLA', 'http://horizon-testnet.kininfrastructure.com', 'Kin Testnet ; December 2018')
client = kin.KinClient(env)
account = client.kin_account('')

@app.route('/whitelist', methods=['POST'])
def whitelist():
    whitelist_request = flask.request.get_json()
    whitelisted = account.whitelist_transaction(whitelist_request)
    return whitelisted, 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)
