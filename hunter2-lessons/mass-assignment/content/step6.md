# Protecting Data with Orator Models

In the other two solutions we reviewed in the previous step, there were issues with having the checks and validation scattered throughout the codebase. Since higher code complexity introduces the potential for more security issues, a simpler approach to this problem is going to be better than a complex one. Fortunately, tools like [Orator](https://orator-orm.com) have just what we need.

Previously the code was making use of plain JSON to store the user data but in a larger application, a much more common source is a database. The Orator library provides easy access to information in a database following the [Object Relational Mapping](https://en.wikipedia.org/wiki/Object-relational_mapping) design pattern. Since we'll be making use of this library, the application will switch to use a SQLite database instead of the JSON.

The Orator library solves the mass assignment issue by including functionality to define "fillable" columns. This configuration lets the developer define which columns can be updated with an array of data pushed into the object rather than having to assign the properties manually. In order to change over from using the JSON `userManager` and use the new Orator-based one, update your imports in `app.py`:

```
# Remove this
import user_json as userManager
# And replace with this
import user_db as userManager
```

This resets the `userManager` alias to use the one from the `user_db.py` module instead. Go ahead and open up the `user_db.py` file and you'll see methods with the same interfaces as the other manager. There's one main difference here, though. In the `imports` this manager pulls in the `User` model (an Orator data model) and uses that to insert/update the data. In `user.py`, the model is defined:

```
import db

class User(db.Model):

    __fillable__ = ['name', 'email', 'password']
```

The `__fillable__` property defines which values can be set via an update without the need to manually define each property.

If you try the same `curl` command as before, you'll notice that the `username` value does not update. That's because it's not a "fillable" field according to the `User` model and is just dropped.
