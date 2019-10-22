# Bypass of correct validation with `alg` change to None

### Algorithms and None

Now that we've learned some about the structure and contents of JWTs, we're going to get into the fun stuff. The reminder of this lesson will guide you through two different vulnerabilities that were found in the JWT spec that, without the knowledge of how to avoid them, could allow an attacker to bypass the control completely (or inject their own information into the claims).

In this first vulnerability, we're going to focus on the `alg` setting in the header JSON. While the JWT specification includes information about the HMAC and RSA signature generation methods, it also includes an "interesting" value: the `None` algorithm. In essence, this algorithm was designed to allow the creation of completely trusted tokens that do not require signature validation. In practical application, this essentially means that, regardless of what the signature is, there's no reason to validate it.

This is a huge problem considering that it's so easy for an attacker to change the JWT header to `alg:"None"` and bypass the signature checking completely, allowing an attacker to update the content as much as they want.

### Performing the attack

Lets see how we can perform this exploit on our example "Users" API. First, so ahead and make a request to the `{$VIRTUAL_HOST}/login` endpoint as a `POST` request and send the following information:

```
username=user1&password=test1234
```

This should successfully log you in and return a `message` value with a `token`. This is the JWT token for your current session. You can then [decode it](https://jwt.io/) and find that the `alg` value is `HS256` meaning it will use HMAC hashing for the signature. In a normal situation, we'd need to know the secret to update the signature, but we don't even need that with `alg:"None"`.

Take the `header` and `claims` payload and recreate the first to parts of the token:

```python
import base64
header = base64.b64encode('{"alg": "None", "type": "JWT"}'.encode('utf-8'))
payload = base64.b64encode('{"claims": {"username": "user1", "level": "admin"}}'.encode('utf-8'))
```

These `header` and `payload` values can then be combined along with an empty signature and used as the token:

```
eyJhbGciOiAiTm9uZSIsICJ0eXBlIjogIkpXVCJ9.eyJjbGFpbXMiOiB7InVzZXJuYW1lIjogInVzZXIxIiwgImxldmVsIjogImFkbWluIn19.
```

Since we're changing the `alg` the system will use to verify the signature, it doesn't matter if it exists or not. Just make sure the token ends in a period so the parser will correctly see it as having three parts (one of the first things many check for).

Make a request to the `{$VIRTUAL_HOST}/users` endpoint using this token as the `X-Auth-Token` header value and see what you get:

```
curl --request GET --url {$VIRTUAL_HOST}/users \
  --header 'X-Auth-Token: eyJhbGciOiAiTm9uZSIsICJ0eXBlIjogIkpXVCJ9.eyJjbGFpbXMiOiB7InVzZXJuYW1lIjogInVzZXIxIiwgImxldmVsIjogImFkbWluIn19.'
```

Since we updated the `level` value in the token's claims to `admin` you should receive a full listing of both users, not just your own information.

### Why does this work?

This attack works for two reasons. First, the functionality that is being used to parse the incoming token has implemented all of the possible algorithms, including `None`. Second, it is blindly using the algorithm defined in the token, assuming it's the one that's intended without doing any secondary verification.

When this issue was first brought more into the public eye (see [this report](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/)) several of the more widely used libraries implemented a secondary check that compares the algorithm on the incoming token against the one desired. It then can fail immediately if those don't match, preventing any further bypass. If you find yourself working on JWT functionality or making a package of your own, it would be in your best interested to include this kind of secondary check (and potentially just not supporting `None` at all).

Later in this lesson we'll be covering how to correct this issue making use of an up-to-date package to replace our custom logic.
