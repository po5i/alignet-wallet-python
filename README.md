# Test Alignet Wallet

Provided input data is located on `.env` file.

To setup:
```
cp .env.sample .env
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

And complete the variables on `.env` file.

## Wallet
To test wallet SOAP service:
```
python wallet.py
```

## Transactions
To transactions query:
```
python transactions.py
```

## Send data
To test web app to send data to VPOS2:
```
python web.py
```
And open this url on the browser: `http://localhost:5000/send`, You need to provide an unique `PURCHASE_OPERATION`.

Sadly you cannot provide the response url, so it will try to load `http://localhost/BNCRModal/recepcion_vpos2.php`


## Receive data
To test response from VPOS2, keep running the server and use curl command or import this on postman:
```
curl -X POST \
  http://localhost:5000/receive \
  -H 'Cache-Control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F purchaseVerification=433e9b4eb30ae221b8a704851aedb91cc6f990ccc2939c1c235c6e341b0ef38ad37dce3851524454c4097ac248af46c78c76f5338ed55ded02990bfa25a78ff5 \
  -F acquirerId=99 \
  -F idCommerce=8056 \
  -F purchaseOperationNumber=000000027 \
  -F purchaseAmount=1000 \
  -F purchaseCurrencyCode=840 \
  -F authorizationResult=00
  ```
You will see the output on the console.
