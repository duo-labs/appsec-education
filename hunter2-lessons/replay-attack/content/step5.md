# Breaking the Pattern

### Introducing Randomness

As we saw in the previous example, if there's no randomness introduced into our requests, the same request can be executed over and over regardless of the "signature" security control. Now we need to fix this so the attacker can't just directly replay the request, but how?

A simple way is to introduce some kind of randomness into the hashing that's performed as a part of the signature validation. One easy way to do this is to use a value that's common between a server and client: the current time. This is a constantly changing value that's never the same twice (if you use the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time)) and, in most languages, can be defined down to the micro- or millisecond. Using this value also has an added benefit of reducing the amount of time that the request is valid for, not just making it difficult to reproduce.

### Code Talking Time

So, lets update our code for both the server and the client to inject this value into the hash creation and validation. Open the `app.py` and locate the `Users` class where the `/user` endpoint request is handled. Currently the code pulls the `data` from the request and uses the `secret` provided to regenerate the hash for verification.

First, to be able to use the time functionality we need to import the `time` module into the script. Add this line to the top of the file:

```
import time
```

Now we can use it later in the signature creation/validation as an extra piece of the secret:

```
data = request.data
ms = int(time.time())
secret = user['secret'].encode('utf-8') + str(ms).encode('utf-8')

digest = hmac.new(secret, data, hashlib.sha256).hexdigest()
```

In the code above, we're adding the Unix epoch time in seconds to the secret that's provided to make the result more randomized. The resulting signature would be different every time, preventing a direct replay of the request. We can then modify our Python client to match this new logic:

```
ms = int(time.time())
secret = secret + str(ms)

# Make the signature
digest = hmac.new(secret, data, hashlib.sha256).hexdigest()
headers = {
    'X-Session': session,
    'X-Signature': digest
}
```

This solves the problem of randomness in the requests but does it solve replay attacks completely? Unfortunately, no and in the next section we'll find out why.
