# Introduction to JSON Web Tokens

### What they are

As web applications have evolved, the authentication and authorization controls they require have improved right along with them. Back in the day, a simple username and password combination were sufficient to protect a system. We've come a long way from there, though. Now systems are more complex and more connected than ever with each other. It's because of these connections and more complex requirements that newer technologies, like JSON Web Tokens, have been defined and have become a popular security control in modern applications. 

A JSON Web Token (or JWT) is a data structure, [defined in an RFC](https://tools.ietf.org/html/rfc7519), that defines a "compact, URL-safe means for representing claims between two parties". A JWT can be used to replace some of the functionality usually provided by sessions and session identifiers. It provides more context than a simple, single session ID can provide by embedding information - or "claims" - into the token itself rather then relying on querying backend storage for authentication and authorization details.

### How they're used

While JSON Web Tokens are flexible enough to be used in many different types of systems, you'll see them most commonly used as:

- An authentication control for APIs
- Server-to-server authentication
- (Non-sensitive) state management in single-page applications

There's also some things that they *shouldn't* be used for. For example, JWTs are *not* a good replacement for sessions. Sessions often contain sensitive data the user should not be able to view or manipulate. This data is best left out of the eyes of the user (and potential attackers).

> Sensitive data should **never** be included in the claims section of a JWT token

Usually, once the tokens have been generated, they'll be sent along with future requests as `Authorization` headers.
