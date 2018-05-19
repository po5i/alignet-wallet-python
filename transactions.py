import os
import hashlib
import requests
import pprint
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Parameters
acquired_id = os.getenv('ACQUIRERID')
id_commerce = os.getenv('ID_COMMERCE')
purchase_operation = os.getenv('PURCHASE_OPERATION')
secret_key = os.getenv('SECRET_KEY_2')

# Compute verification
data = '{}{}{}{}'.format(acquired_id, 
                         id_commerce, 
                         purchase_operation, 
                         secret_key)
m = hashlib.sha512()
m.update(data.encode())
verification = m.hexdigest()

endpoint = 'https://integracion.alignetsac.com/VPOS2/rest/operationAcquirer/consulte'
headers = {
    'Content-type': 'application/json'
}
data = {
    'idAcquirer': acquired_id,
    'idCommerce': id_commerce,
    'operationNumber': purchase_operation,
    'purchaseVerification': verification
}
response = requests.post(endpoint, json=data, headers=headers)
json_response = response.json()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json_response)