import os
import hashlib
from dotenv import load_dotenv
from flask import Flask
from flask import render_template


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