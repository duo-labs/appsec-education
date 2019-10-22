import jwt
from jwt import InvalidSignatureError
import user_db as userManager
from jwt.algorithms import RSAAlgorithm

use_secret = b's3cr3t'
# use_algorithm = 'HS256'
use_algorithm = 'RS256'

def generate(data):
    if use_algorithm == 'HS256':
        secret = use_secret

    elif use_algorithm == 'RS256':
        username = data['username']
        secret = open('keys/'+username+'/private.pem', "r").read().strip()

    token = jwt.encode(data, secret, algorithm=use_algorithm)
    return token

def parse(token):
    # Find the user with the token
    user = userManager.findByToken(token)
    if not user:
        return False

    try:
        if use_algorithm == 'HS256':
            secret = use_secret
        
        elif use_algorithm == 'RS256':
            secret = open('keys/'+user.username+'/public.pem', "r").read().strip()
            
        return jwt.decode(token, secret, algorithms=[use_algorithm])

    except (InvalidSignatureError):
        return False
