# Requests and Replays

### Making an authenticated request

Now that we know how to log in to the API, we can make a request to get the list of users. As the documentation shows, you'll need to take the `session` and `secret` values and use them to generate a signature for the request. This value is used to generate a `SHA256` hash signature that's sent along with the request as the `X-Signature` value (with the session ID).

Here's a Python script that shows how this works:

```
import requests, hashlib, hmac

url = '{$VIRTUAL_HOST}/users'
session = '<session ID here>'
secret = '<secret value here>'
data = ''

# Make the signature
digest = hmac.new(secret, data, hashlib.sha256).hexdigest()
headers = {
    'X-Session': session,
    'X-Signature': digest
}
r = requests.get(url, headers=headers)

print('Return status: {}'.format(r.status_code))
print(r.text)
```

First you'll need to make a `/login` request and grab the `session` and `secret` values. Plug those into the script above and it will use them along with the request payload (in this case an empty string) to make the hash. This value along with the session is sent with the request and the list of users is returned as JSON.

### Performing the Replay

So, after all this you may be saying to yourself "I thought we were going to learn about replay attacks!" Well, now's the time. Lets take a closer look at the request being sent to fetch the user listing. When we build out the signature so our message will verify, we use the secret and the data to make the `SHA256` hash. 

`SHA256` hashes, much like many other hashing methods, will return the same hashed version when the same input is used. If an attacker were sitting on the network and somehow performed a man-in-the-middle attack and intercepted the contents of this request (headers and all), there's nothing in that message preventing them from making the same request over and over - *replaying it* - as many times as they'd like.

In this case, we're only performing a `GET` request, but remember the `POST` example earlier where you could transfer as much money as you wanted just by replaying the same request? Even with a signature check like we've implemented on our API, that same attack is possible! There's nothing changing between the requests so an attacker could reuse the same request as long as the session is valid.

Now we'll look at one simple thing we can do to help prevent an attack like this by adding in some randomness.


