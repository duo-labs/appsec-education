import json, base64, hashlib, hmac

username = 'user1'
pubkey = open('keys/'+username+'/public.pem', "r").read().strip()

header = base64.b64encode('{"alg": "HS256", "type": "JWT"}'.encode('utf-8'))
payload = base64.b64encode('{"claims": {"username": "user1", "level": "admin"}}'.encode('utf-8'))

# And now the signature
message = '{}.{}'.format(header, payload).encode('utf-8')
signature = hmac.new(pubkey.encode('utf-8'), message, hashlib.sha256).hexdigest()

token = [
    header.decode('utf-8'),
    payload.decode('utf-8'),
    signature
]
token = '.'.join(token)

print(token)
