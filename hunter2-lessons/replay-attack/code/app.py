from flask import Flask, render_template, request, make_response
from flask_restful import Resource, Api

import sys
import user_manager
import bcrypt
import hashlib
import os
import hmac
# from Crypto.Hash import SHA, HMAC

app = Flask(__name__)
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

        user = user_manager.findByUsername(username)
        if user == False:
            return jsonFail('Login failed', 401)

        user_password = user['password'].encode('utf-8')

        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user_password):
                # Generate the SHA1 and update the user record
                header = hashlib.sha256()
                header.update(os.urandom(64))

                session = hashlib.sha256()
                session.update(os.urandom(64))

                data = {
                    'secret': header.hexdigest(),
                    'session': session.hexdigest()
                }
                user_manager.save(user['id'], data)

                return {
                    'success': True,
                    'message': {
                        'secret': header.hexdigest(),
                        'session': session.hexdigest()
                    }
                }
            else:
                return jsonFail('Login failed', 401)
        else:
            return jsonFail('Login failed', 401)

class Register(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        user = user_manager.findByUsername(username)
        if user:
            return jsonFail('User must be unique.', 400)

        user_manager.addUser({
            'username': username,
            'password': bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
        })

        return {'success': True, 'message': 'User succesfully registered.'}

class Users(Resource):
    def get(self):
        # Make sure the header is set and that it matches a user record
        headers = request.headers

        if ("X-Signature" not in request.headers or "X-Session" not in request.headers): 
            return jsonFail('Valid authorization headers required', 400)

        session = request.headers.get('X-Session').strip()
        signature = request.headers.get('X-Signature').strip()

        user = user_manager.findBySession(session)
        if not user:
            return jsonFail('Invalid session', 401)

        # Calculate the hash of the request and compare
        data = request.data
        secret = user['secret'].encode('utf-8')
        digest = hmac.new(secret, data, hashlib.sha256).hexdigest()

        if digest != signature:
            return jsonFail('Signature failure', 400)

        return {
            'users': user_manager.getAll(),
            'success': True
        }

class Transfer(Resource):
    def post(self):
        # Make sure the session header is set
        headers = request.headers

        if ("Session" not in request.headers):
            return jsonFail('Valid authorization headers required', 400)

        if not request.form['to']:
            return jsonFail('Valid "to" account required', 400)

        if not request.form['amount']:
            return jsonFail('Valid "amount" required', 400)

        amount = request.form['amount']
        return {
            'messsage': 'Transfer of ${} successful!'.format(amount),
            'success': True
        }


api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Users, '/users')
api.add_resource(Transfer, '/transfer')
