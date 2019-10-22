# User Editing and Exploiting

Now lets take a look a user editing. Close any file you might have open and go back and open the `app.py` again. Scroll down and look for the routes for `/user/edit/<user_id>` - there's two, one for the `GET` and the other for the `POST` to perform the save action.

Much like with our "Add New User" handling, when the edit form is submitted it is handled by the `POST` route. This time, however, it uses the `userManager.save` method to save the incoming data back to the user record identified by the `user_id` value. The data comes from the special `request.form` property of Flask's request object handling.

Close the `app.py` file and re-open the `user_json.py` file and locate the `save` method (just below the `addUser` method). In this method, the code parses the JSON from the file, tries to locate the user record and - if found - updates the data including using `bcrypt` hashing on the password. It then finishes by pushing these changes into the user record and writing the object structure back out to JSON.

Did you spot the issue with the current code and how a mass assignment vulnerability could happen? Here's a hint: there's no `username` field in the user edit form. When the form is submitted, the values for `name`, `email` and `password` are handled by the `POST` route and the `update` method. However, since HTTP requests are just plain-text and can be easily edited, it's not difficult to change a request to include one extra field: the `username`.

The easiest way to perform this exploit is to make use of a command line `curl` call. Open a terminal window and copy and paste the following in:

```
curl 'http://{$VIRTUAL_HOST}}/user/edit/1' -H 'Content-Type: application/x-www-form-urlencoded' \
--data 'username=test&name=User+1&email=user1%40test.com&password=test'
```

This command sends the `POST` request to the `/user/edit/1` endpoint, taking all of the data provided and pushing it into that `update` method. Since we're not doing any kind of input validation or unsetting the `username` value in any way before the update, the `username` value we provided in the `curl` request is updated right along with the rest of the data.

Congratulations! You've just updated a piece of data - the `username` - the developer of the system didn't intend for you to be able change. Now that we've seen how to exploit this issue, lets see some methods to fix it.
