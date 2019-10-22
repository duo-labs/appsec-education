# Fixing the exploit

Up until now, we've been testing the web application externally to locate the vulnerability. In order to fix the issue, we'll need to dive into the code and change a few things. Our main application resides in the `app.py` file so go ahead and open that using this command:

```
pico app.py
```

The application is relatively small thanks to Flask. There are two routes defined, one for the main `/` endpoint and another for our `/vulnerable` endpoint. In the code for the `/vulnerable` endpoint, you'll see that it checks for the `username` value first. If found it continues on and looks for the newline (either `\n` or `\r`) and, if found, detects it as exploited. If the `username` value looks okay, it simply outputs it as normal.

In order to fix the exploit, we need to remove the issue newlines can cause from the user input. In theory, this is as simple as removing any `\n` or `\r` characters with a string replacement but there's a more correct way to do that when the tools are provided for you. Flask already has a way of setting headers using `response.headers`. This goes through a set of checks to make sure invalid content isn't present in the string automatically. We want to use this rather than rolling our own for consistency so we can replace the current content of the `/vulnerable` route with the following:

```
@app.route("/vulnerable")
def vulnerable():
    username = request.args.get('username')
    response = make_response(render_template('vulnerable.html', username=username))

    if username != None:
        response.headers['X-Username'] = '%s' % username

    return response
```

Now if you try the same attack using `username=test%0AX-Exploited:%20123` you'll get an error from Flask itself. Its built-in security controls detected the newline in the value and threw an error.

## Check

`grep 'response.headers' /home/whitehat/web/app.py | wc -l | { [[ $(cat) -ge 1 ]] && echo yes; }`