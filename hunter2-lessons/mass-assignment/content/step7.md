# In Summary

Making use of functionality already included in Orator to prevent mass assignment issues provides consistency and simplicity across the entire application. Any place the `User` model class is used, the `fillable` protection will kick in.

One question you might be left with, though, is how to set that `username` value if it's not in the allowed list for filling. If you'll remember the second suggested fix from the list before, you'll have your answer (or just look in the `addUser` method of `user_db.py`): manual assignment. As this method is a more direct way of setting those values, the model doesn't check if a value is "fillable" or not.

In this tutorial we've walked through what a "mass assignment" vulnerability is, where the problem comes from and some potential solutions to help prevent it. In this case, the database library chosen came with the "fillable" functionality included but not all do. Be sure to verify how a library handles mass data updates like this to ensure you're not introducing this kind of vulnerability into your system.
