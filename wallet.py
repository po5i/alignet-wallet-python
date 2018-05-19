import os
import hashlib
from zeep import Client
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Parameters
id_ent_commerce = os.getenv('ID_ENT_COMMERCE')
cod_cardholder_commerce = os.getenv('COD_CARDHOLDER_COMMERCE')
name = os.getenv('NAME')
last_name = os.getenv('LAST_NAME')
mail = os.getenv('MAIL')
reserved1 = os.getenv('RESERVED1')
reserved2 = os.getenv('RESERVED2')
reserved3 = os.getenv('RESERVED3')
secret_key = os.getenv('SECRET_KEY')


# Compute verification
data = '{}{}{}{}'.format(id_ent_commerce, 
                         cod_cardholder_commerce, 
                         mail, 
                         secret_key)
m = hashlib.sha512()
m.update(data.encode())
verification = m.hexdigest()

# Wallet WSDL
params = (
    id_ent_commerce,
    cod_cardholder_commerce,
    mail,
    name,
    last_name,
    reserved1,
    reserved2, 
    reserved3,
    verification
)

wsdl = 'https://integracion.alignetsac.com/WALLETWS/services/WalletCommerce?wsdl'
client = Client(wsdl)
result = client.service.RegisterCardHolder(*params)

print('Response code: {}'.format(result['ansCode']))
print('Description: {}'.format(result['ansDescription']))
print('Association code: {}'.format(result['codAsoCardHolderWallet']))
print('Date: {}'.format(result['date']))
print('Time: {}'.format(result['hour']))