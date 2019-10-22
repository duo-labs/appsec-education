from flask import Flask, render_template, request, make_response
import werkzeug, bcrypt
from flask_orator import Orator

import user_json as userManager

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'sqlite',
        'database': '/tmp/test.db'
    }
}
db = Orator(app)

## ------------------

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', users=userManager.getAll())

@app.route("/", methods=['POST'])
def indexSubmit():
    password = request.form['password'].encode('utf-8')

    userManager.addUser({
        'username': request.form['username'],
        'password': str(bcrypt.hashpw(password, bcrypt.gensalt())),
        'name': request.form['name'],
        'email': request.form['email'],
    })

    return render_template('index.html', users=userManager.getAll())

@app.route("/user/edit/<user_id>", methods=['GET'])
def userEdit(user_id):
    return render_template('edit.html', user=userManager.findById(user_id))

@app.route("/user/edit/<user_id>", methods=['POST'])
def userEditSubmit(user_id):
    userManager.save(user_id, request.form.to_dict())
    return render_template('edit.html', user=userManager.findById(user_id))
