# Fixing the Glitch

### Shifting to PyJWT

Our current JWT creation and parsing implementation happens in the "JWT manager" functionality in the `jwt_custom.py` file. In order to switch over to using the package, this file will need some pretty significant updates. Fortunately, the PyJWT library handles a lot of the logic for us and will reduce the amount of code significantly.

First lets make sure the `pyjwt` package is installed. Use the following command in the terminal to make sure we have it:

```
pip install pyjwt
```

If it's not already installed it should run through a quick download and installation process to get the package configured and ready to use. Now we can move on to the code. If you open the `jwt_lb.py` file you can see our updated code that makes use of the `pyjwt` library. As you can see, it's much shorter and easier to follow (less complexity makes for less potential bugs).

Our same `generate` and `parse` functions are there but there's one big change that helps to prevent the issues from before: the algorithm to use is hard-coded (`use_algorithm`) instead of being detected from the `header` content of the token. 

### Using the new code

There's one slight change to make to our application so we can use this new code. Before the code was importing the `jwt_custom` file as the `userManager`. Update the line near the top of the `app.py` file that performs the import to this:

```
import jwt_lib as jwtManager
```

### Preventing None and RSA-to-HMAC

Using this hard-coded value prevents both the RSA-to-HMAC switching vulnerability and the use of `None` that we've shown make the system vulnerable. At the end of the call to `jwt.decode` inside of `parse` there's another control added: the use of the `algorithms` parameter. We're populating this with only our allowed algorithm, locking it down regardless of what the `header` says.

The PyJWT library has solved the user-controlled algorithm issue by being "opt-in" for which algorithm it allows.

Go ahead and try our two attacks against this new code and see if either of them still work! Also try switching the `use_algorithm` value back and forth to see the protection work for both issues.
