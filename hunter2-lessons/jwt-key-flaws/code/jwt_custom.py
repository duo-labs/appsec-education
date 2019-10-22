import json, base64, hashlib, hmac
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

hmacSecret = b's3cr3t'
useAlgorithm = 'HS256'
# useAlgorithm = 'RS256'

def generate(data):
    header = {
        'alg': useAlgorithm,
        'typ': 'JWT'
    }
    payload = {
        'claims': data
    }
    # JSON and base64 encode content
    json_header = base64.b64encode(json.dumps(header).encode('utf-8'))
    json_payload = base64.b64encode(json.dumps(payload).encode('utf-8'))

    # Build message and signature
    message = '{}.{}'.format(json_header, json_payload).encode('utf-8')

    # Get secret source based on desired algorithm
    if useAlgorithm == 'HS256':
        secret = str(hmacSecret).encode('utf-8')

    elif useAlgorithm == 'RS256':
        username = data['username']
        secret = open('keys/'+username+'/private.pem', "r").read().strip()

    # Generate signature based on algorithm
    if useAlgorithm == 'HS256':
        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()

    elif useAlgorithm == 'RS256':
        # Generate the signature using the private key
        rsakey = RSA.importKey(secret)
        signer = pkcs1_15.new(rsakey)
        
        digest = SHA256.new()
        digest.update(message)
        sign = signer.sign(digest)

        signature = base64.b64encode(sign).decode('utf-8')

    # Combine them to get the token
    token = [
        json_header.decode('utf-8'),
        json_payload.decode('utf-8'),
        signature
    ]
    token = '.'.join(token)

    return token.encode('utf-8')

def parse(token):
    parts = token.split('.')
    json_header = json.loads(base64.b64decode(parts[0]).decode('utf-8'))
    json_payload = json.loads(base64.b64decode(parts[1]).decode('utf-8'))
    algorithm = json_header['alg']
    message = '{}.{}'.format(parts[0].encode('utf-8'), parts[1].encode('utf-8')).encode('utf-8')

    # Get secret source based on our desired algorithm
    if useAlgorithm == 'HS256':
        secret = hmacSecret

    elif useAlgorithm == 'RS256':
        username = json_payload['claims']['username']
        secret = open('keys/'+username+'/public.pem', "r").read().strip()

    # Verify the signature based on the algorithm type provided in the token
    if json_header['alg'].lower() == 'none':
        return json_payload

    elif algorithm == 'RS256':
        # Verify it using RSA keys
        rsakey = RSA.importKey(secret)
        digest = SHA256.new(message)
        signature = base64.b64decode(parts[2])

        try:
            pkcs1_15.new(rsakey).verify(digest, signature)
            return json_payload
        except (ValueError, TypeError):
            return False

    elif algorithm == 'HS256':
        # Regenerate signature to ensure validity then return
        secret = str(secret).encode('utf-8')

        signature = hmac.new(secret, message, hashlib.sha256)

        if signature.hexdigest() != parts[2]:
            return False
        else:
            return json_payload
    else:
        return False
