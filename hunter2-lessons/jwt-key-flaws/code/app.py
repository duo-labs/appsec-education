from flask import Flask, render_template, request, make_response
from flask_restful import Resource, Api
from flask_orator import Orator
import bcrypt, jwt, base64, hashlib, hmac, json

app = Flask(__name__)

import user_db as userManager
import jwt_custom as jwtManager
# import jwt_lib as jwtManager

app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'sqlite',
        'database': '/tmp/test.db'
    }
}
db = Orator(app)
api = Api(app)

def jsonFail(message, code=500):
    return {
        'success': False,
        'message': message
    }, code

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = userManager.findByUsername(username)

        if user:
            user_password = user.password.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), user_password):
                # Make the token and store it in the user record
                data = {
                    'username': user.username,
                    'level': user.level
                }
                token = jwtManager.generate(data).decode('utf-8')
                userManager.save(user.id, {
                    'token': token
                })

                return {
                    'success': True,
                    'message': {'token': token}
                }

        return jsonFail('Invalid credentials provided', 400)

class Users(Resource):
    def get(self):
        if 'X-Auth-Token' not in request.headers:
            return jsonFail('Required auth header not provided', 400)

        # Decode the token and use the level for fetching users (trusted)
        token = request.headers['X-Auth-Token']
        result = jwtManager.parse(token)

        if not result:
            return jsonFail('Invalid credentials provided', 400)

        claims = result['claims'] if 'claims' in result else result
        if claims['level'] == 'admin':
            users = userManager.getAll().serialize()
        else:
            user = userManager.findByUsername(claims['username']).serialize()
            users = [user]

        return {'users': users}

class Token(Resource):
    def get(self):
        secret = 'test1234'
        claims = {
            'username': 'user1',
            'level': 'admin'
        }
        message = json.dumps(claims).encode('utf-8')

        header = {
            'typ': 'JWT',
            'alg': 'HS256'
        }
        header = json.dumps(header).encode('utf-8')

        header_b64 = base64.urlsafe_b64encode(header).decode().strip('=')
        message_b64 = base64.urlsafe_b64encode(message).decode().strip('=')

        signing_message = '{}.{}'.format(header_b64, message_b64)
        signature = hmac.new(secret.encode('ascii'), signing_message.encode('utf-8'), hashlib.sha256).digest()

        token = '{}.{}.{}'.format(
            header_b64,
            message_b64,
            base64.urlsafe_b64encode(signature).decode().strip('=')
        )

        return {'token': token}

api.add_resource(Login, '/login')
api.add_resource(Users, '/users')
api.add_resource(Token, '/token')
