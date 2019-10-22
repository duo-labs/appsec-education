# Potential Solutions

In its current state, our application is vulnerable to a mass assignment exploit allowing an attacker to update any information that they'd like. To fix this, there's several things we could potentially do. We can either:

- add in some input validation to make sure they don't submit something they shouldn't
- manually assign values rather than pushing them all in
- use a tool that includes functionality to specifically mitigate mass assignment vulnerabilities

Lets start at the top of the list and work our way down. The first in the list is the addition of input validation. Lets update the code in `app.py` to add some in for the `username` value:

```
@app.route("/user/edit/<user_id>", methods=['POST'])
def userEditSubmit(user_id):
    data = request.form.to_dict()
    if data['username]:
        del data['username']

    userManager.save(user_id, data)
    return render_template('edit.html', user=userManager.findById(user_id))
```

In this updated code, we specifically check for the `username` value in the incoming data and delete it from the set if it exists. Mission accomplished, right? Well, in a sense. In this example, we're handling a check of just one value in just one place. In a simple application like this that's not too much work but imagine what would happen in a complex application with a much larger potential surface area for these checks. It would work but it's going to be difficult to keep all of those checks the same.

Lets move on to the next option: manually assigning values rather than just pushing them in as a set of values. This would involve a change in our `user_json.py` user manager class. In the `save` method we'd need to update the code to replace the `user.update(userData)` with something like this:

```
user['name'] = userData['name]
user['email'] = userData['email']
user['password'] = userData['password']
```

Much like the previous example, this would be effective in mitigating the mass assignment issue as only the intended values are set. However, this also means working with the `user` objects in multiple places and making libraries like this `userManager` less useful.

Is there a good middle ground that combines both the ease of setting an array of data while still protecting from unwanted injections? Fortunately yes, and several data handling libraries include functionality to prevent this issue specifically. The one we're going to look at is a database tool (and ORM) called [Orator](https://orator-orm.com).
