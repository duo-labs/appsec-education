# Fixing the Issue - JSON Parsing

It's clear that there's an issue around the JSON handling in this application we need to fix to prevent Javascript execution. As you found out in the previous step, there are several issues to correct in several places. Lets walk through each of them, moving from the backend out to the frontend.

#### Changing the JSON Parser

Currently the JSON parser in the application is pretty minimal and is done manually via regular expressions. A much better approach is to use the JSON handling built into Python that's much more robust and prevents invalid content and formatting from making it into the data.

We'll need to change the `parseJson` and `writeJson` functions to use this functionality. Update them to use this code instead:

```
def parseJson():
    f = open('data/users.json', 'r')
    data = json.loads(f.read())

    return data

def writeJson(data):
    f = open('data/users.json', 'w')
    f.write(json.dumps(data))

    return True
```

Once you've made these changes, try the same attack again. You'll notice something different about the data provided by `/users`: the `id` value is now handled more correctly and `alert(1)` is quoted as a string. This, in turn, is evaluated by the Javascript `eval` as a string and not valid Javascript code. This means it's no longer executed.