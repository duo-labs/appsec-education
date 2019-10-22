from flask import Flask, render_template, request, make_response
import werkzeug

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/vulnerable")
def vulnerable():
    username = request.args.get('username')

    if username == None:
        resp = make_response('Please provide a valid username')
        return resp

    if "\n" in username or "\r" in username:
        header = 'username=%s' % username
        resp = make_response('Exploited!')
        resp.headers = werkzeug.datastructures.Headers([
            ('X-Username', header)
        ])
    else:
        resp = make_response('Hello %s!' % username)
        resp.headers['X-Username'] = '%s' % username

    return resp

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)