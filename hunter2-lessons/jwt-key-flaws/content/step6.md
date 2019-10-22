# Planning the Fix

### A Recap

So far we've looked at two vulnerabilities present in functionality that the JWT specification defines. One is a by-product of an insecure mechanism and the other is mostly due to the ability of a user to redefine the algorithm used and shift it to cause unintentional behavior.

In its current state, the example application could be corrected and prevent these issues. There's two main changes that could be made to prevent these two vulnerabilities:

- Prevent the use of the `None` algorithm
- Ensure that the algorithm used for parsing and decoding the token is what's expected.

The first change would be a relatively simple one in our `jwt_custom.py` file. It would mean removing these lines:

```python
if json_header['alg'].lower() == 'none':
    return json_payload
```

and updating the `if` check below it to: `if algorithm == 'RS256':`. Making this change would mean that the `alg` value wouldn't match either the `HS256` or `RS256` values and fail the validation.

Make this change and try the `None` attack again and see if it still works.

The second fix is a bit more complicated and would require more complex logic changes than just a few lines like above. We could change the current functionality but why maintain more than we have to when there's other, just as secure options.

### Let's pick libraries

As an alternative to using and maintaining our own code (requiring us to be experts in all things JWT) we could use a library that's been vetted and isn't vulnerable to the two attacks we've covered. Using a library isn't the only way to fix an issue like this, but it can make it simpler and less of a burden on the development teams for future improvements.

Since our application is written in Python, we've opted for the [pyjwt library](https://pyjwt.readthedocs.io/en/latest/). When these vulnerabilities were made public, the pyjwt project made the updates required to prevent them as is referenced in [the comments for this release](https://github.com/jpadilla/pyjwt/releases/tag/1.0.0). This is just one of many potential JWT libraries out there but as this one is known to not be vulnerable, it's an easy choice.

There's plenty of other libraries available for other languages too such as:

- namshi/jose for PHP
- firebase/php-jwt for PHP
- jsrsasign for Javascript
- org.bitbucket.b_c / jose4j / 0.6.3 for Java
- jwt for Ruby
- SermoDigital/jose for Go

The [jwt.io site](https://jwt.io/) also includes a long list of libraries for a wide range of languages so if you don't see one listed above, you can probably find one there.
