# In Summary

### Using third-party code safely

In this lesson two of the main vulnerabilities with JWT tokens have been shown. It walked though what the issues were, how to perform the attack and how they can be prevented. In the case of this lesson, we made use of the PyJWT library to help simplify the process and to provide adequate protection from malicious user updates to the tokens.

While using a library like PyJWT is a good option, any external code needs to be vetted before it's implemented into your system. As mentioned, it's definitely possible to fix these same issues in your own code (and potentially even write your own JWT library), it would just require more knowledge on your part to maintain. If you do go down that road, at least now you're aware that these two vulnerabilities are possible and how to prevent them in your own application.

### Additional Resources

This lesson only touched on some of the topics around JSON Web token security, focusing on two main vulnerabilities in implementations of the base specification. There's also a larger number of signature generation methods besides the HMAC and RSA approaches we've covered here. You can find out more about these other mechanisms in these specifications:

- [Javascript Object Signing and Encryption (JOSE)](https://datatracker.ietf.org/wg/jose/charter/)
- [JSON Web Encryption (JWE)](https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-40)
- [JSON Web Key (JWK)](https://tools.ietf.org/html/draft-ietf-jose-json-web-key-41)

Thankfully, most of the JWT libraries provide functionality to handle these additional methods, making it simpler to enforce stronger protection for your tokens. [This article](https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3) provides a good introductory look at them as well.
