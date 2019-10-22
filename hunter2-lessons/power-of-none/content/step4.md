## Initial State of “code” Value

Now that we've verified that the login and code entry are working correctly, lets take a look at some of the code to see how that value is set. 

### To continue

Open the `app.py` file with the `pico` editor:

```
pico app.py
```

You can see that when a user registers, the `code` value starts with a default value of `None`. When the first part of the login is completed, this value is updated to the randomly generated value. When the user submits the `/user/code` page with the username and code, the values are matched and, if successful, the login process is completed.
