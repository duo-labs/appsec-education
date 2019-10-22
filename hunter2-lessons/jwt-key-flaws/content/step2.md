# How they're structured and created

### The Structure of JWTs

There were some brief mentions in the previous step about the sections of a JWT token and the information they could contain. Lets get into a bit more detail here so you'll understand how they're structured and built.

First off, true to their name, JWTs are built from JSON structured data and are broken up into three sections:

- the header that defines the type of token and the algorithm to use for computing the signature
- the claims section that contains [RFC-defined](https://tools.ietf.org/html/rfc7519#section-4) details and allows for custom data too
- the signature of the token

An example `header` section might look like:

```
{"type": "JWT", "alg": "HS256"}
```

And an example `claims` section:

```
{
    "sub": "Login",
    "exp": "1408621000",
    "test": true
}
```

Where the `sub` and `exp` are RFC-defined claim types and `test` is a custom claim. These JSON structures are then (URL-safe) base64 encoded. These are concatenated with a period (`.`) and a signature is generated using this string as the source. How the signature is generated depends on the algorithm in the `header`. There are several different methods, more than can easily be listed here but the two we'll cover in this lesson are: HMAC hashing and RSA signing. The signature and the two other sections are then joined with periods (`.`).

When a JWT is verified, the token is split on the periods, breaking it into three different sections. The `header` and `claim` information is then reversed back to their JSON state and the signature is regenerated from this data and checked for a match.

### A word about algorithms

There are two things to keep in mind about the algorithm you choose when creating JWTs. First, the algorithm is for generating the signature only and is not used to protect the claim data. All claim data can still be easily decoded in a normal JWT token. Second, the `header` can always be decoded as well so the algorithm in use isn't "secret".
