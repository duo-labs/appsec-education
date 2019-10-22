# An API Example

### Registering a User

First we need to find out more information about our "users" API and how to use it. Make sure your environment is started up correctly and browse over to the main page at `${VIRTUAL_HOST}`. This should display a page with details about registering a new user, authenticating to the API and getting a listing of current users.

The end goal is to get a listing of current users from the API and their details from the `/users` endpoint.

To start using the API, lets register a user. Using your tool of choice (something like [curl](https://curl.haxx.se/) or the Python [requests](http://docs.python-requests.org/en/master/) library) make a request to the `/register` endpoint with the user information:

```
curl -X POST \
    -d "username=testuser1&password=mypassword" \
    {$VIRTUAL_HOST}/register
```

You should receive a successful response with a message about the user `testuser1` being registered.

### Logging In

Now that we have a user in the system, we can authenticate using it so we can start up our session. To do this we make a request to the `/login` endpoint with our `username` and `password` values:

```
curl -X POST \
    -d "username=testuser1&password=mypassword" \
    {$VIRTUAL_HOST}/login
```

The successful response to this request will contain the `secret` and `session` values that we'll need to use in future requests, such as the one to the `/users` endpoint. We'll use this information in the next step: making a request using the instructions in the "Authentication" section of the documentation.


> cat /var/log/nginx/access.log | grep 'POST /login HTTP/1\.1\" 200 ' | wc -l | { [[ $(cat) -ge 1 ]] && echo yes; }
