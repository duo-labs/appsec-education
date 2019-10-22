# Bypass of correct validation with `alg` change to use HMAC

### Making Signatures: HMAC vs RSA

In the previous sections, we learned about a bypass that could be performed by changing the `alg` value to `None` and bypassing any signature validation. Now we're going to look at another potential issue that stems from the same root cause, a change in algorithm, but can be used even if the `None` functionality is disabled.

It was previously mentioned that the default JWT signature generation defined two main ways: HMAC hashing and RSA cryptographic signing. With HMAC hashing, a single "secret" value is used as the key along with the data from from header and claims to create the signature. The RSA signing works in a similar way but makes use of public and private keys to handle the generation and verification (respectively).

Public keys, by their nature, are something that's easy to obtain and aren't particularly secure by themselves. The magic of them comes in when you use that along with the private key to cryptographically verify that there's a match. In the case of this vulnerability, the public availability of the public key is a major part of the problem.

### Exploiting RSA signing

In this example, we're going to generate and verify a JWT using the RSA method with some pre-defined keys. This will use the PyCrypto package for signature generation and verification. To switch over to using this method, open the `jwt_custom.py` file and update these lines (commenting one and uncommenting the other):

```
# useAlgorithm = 'HS256'
useAlgorithm = 'RS256'
```

This tells the code in the file below to use the RSA method (`RS256`) with a `SHA-256` hashing method to create the signature string. Go ahead and make the same `/login` and `/users` request as a normal user would and see what the token looks like. The signature string is a different length but overall it should seem mostly the same.

Now for the exploit - the real trick here is, once again, in the ability to change the `alg` value in the `header` section. If you change it from `RS256` over to `HS256` an interesting thing happens in most token processing. Before it was using the public and private key to verify the string cryptographically. When we switch over to the HMAC algorithm, the public key now becomes the "secret" used in generating the signature hash! This means that, because we have the readily available public key, we can now easily generate our own token with updated claim information and still have it pass validation.

### Building the token

Rather than trying to walk through all of the steps needed to create a compromised token, a script has been provided for you. This Python script reads in the user's public key, uses it as a secret for the HMAC hash and updates the `admin` claim much as was done in the previous example.

To run this script and get the token, use this command:

```
python3 forge_token.py
```
 The token that's spit back out has two changes included: the `alg` value has been updated to use HMAC hashing and the `admin` claim now elevates the user to Administer level access. If you make the request to the `/users` endpoint with this token, you should receive a listing of all user data, not just your own.
