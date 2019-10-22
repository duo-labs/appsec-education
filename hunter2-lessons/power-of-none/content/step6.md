## Fixing the Comparison

There are a few ways to fix this issue but we’re going to focus on changing the “secureCompare” method as a centralized place to prevent this issue from popping up in other places too.

Since the issue is the comparison of the string “None” and the Python constant None, we need to ensure that the two values we’re being provided are of the same type. In this case, we need to be sure they’re both strings. 

### To continue

Try updating the `secureCompare` function so that the result of the comparison function is correct when the inputs are a string of "None" and the `None` Python constant. The function is a "helper" function located near the bottom of the file (at line 143). Make your changes and save the file.

If you'd like to test your changes, you can use this simple command-line `python3` call:

```
python3 -c "import app; print(app.secureCompare('None', None))"
```

When the function does its job correctly, this should return `False` and you will be able to move on to the next section.
