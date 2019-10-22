## Hack the “code”

The `code` value is the key to the problem. Once the user successfully logs in and complete the code verification, their `code` value is set back to `None`. If a user doesn't submit a value for the `code` field in the form, the verification then sets the `code` value to `None` (the Python constant, not the string value).

If the attacker were to visit the `/user/code` page directly and enter in just the username and submit the form, the two values - `None` the string and `None` the constant - are then passed to the `secureCompare` method for evaluation.

Inside of the `secureCompare` method, a byte length comparison of the two values is performed, ensuring they’re the same. However, in the case of either a new user or a user that has already logged in, their `code` value is “None”. When this is compared to the Python constant value of `None`, the bytes of the two strings are equal so the match is successful. 

### Why is this a problem?

Since this final step is all that’s required to successfully log in the user, an attacker can bypass the code requirement by not submitting a value for the `code` in the form and successfully log in as any user.

### To continue

Try submitting the form without a value for the `code` field, only filling in the username, and see what happens.
