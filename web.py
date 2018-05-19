import os
import hashlib
import pprint
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request


app = Flask(__name__)
load_dotenv()

# Parameters
acquirer_id = os.getenv('ACQUIRERID')
id_commerce = os.getenv('ID_COMMERCE')
purchase_operation = os.getenv('PURCHASE_OPERATION')
currency_code = os.getenv('PURCHASE_CURRENCY_CODE')
secret_key = os.getenv('SECRET_KEY_2')
 
@app.route('/')
def hello():
    return 'Alignet Send and receive test!. Go to /send or /receive'

@app.route('/receive', methods=['POST'])
def receive():
    purchase_verication = request.form.get('purchaseVerification')

    # Compute verification
    data = '{}{}{}{}{}{}'.format(request.form.get('acquirerId'),
                                 request.form.get('idCommerce'), 
                                 request.form.get('purchaseOperationNumber'),
                                 request.form.get('purchaseAmount'),
                                 request.form.get('purchaseCurrencyCode'),
                                 request.form.get('authorizationResult'),
                                 secret_key)
    m = hashlib.sha512()
    m.update(data.encode())
    verification = m.hexdigest()

    print('request POST:')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request.form)

    if verification == purchase_verication:
        return 'Verification OK: {}'.format(json.dumps(request.form))
    else:
        return 'Failed verification'

@app.route('/send')
def send():
    # ammount
    ammount = 1000

    # Compute verification
    data = '{}{}{}{}{}{}'.format(acquirer_id, 
                                 id_commerce, 
                                 purchase_operation,
                                 ammount,
                                 currency_code,
                                 secret_key)
    m = hashlib.sha512()
    m.update(data.encode())
    verification = m.hexdigest()

    context = {
        'acquirer_id': acquirer_id,
        'id_commerce': id_commerce,
        'purchase_operation': purchase_operation,
        'ammount': 1000,
        'currency_code': currency_code,
        'verification': verification
    }
    return render_template('send.html', context=context)
 
if __name__ == '__main__':
    app.run()