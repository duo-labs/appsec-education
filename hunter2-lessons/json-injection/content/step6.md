# Fixing the Issue - Javascript Eval()

The backend Python code has been fixed to use the more robust parser, but that only fixes part of the issue. If you'll remember from the description of the exploit, there was also a problem with the frontend code. The Javascript was making use of the `eval()` function to parse the JSON. Because this function is designed to execute the string it's given as code, this still poses a large risk should another method of modifying that JSON be available.

In order to fix this issue, we're going to approach it how we approached the backend: by looking for native functionality that can be used to more correctly parse the JSON so we can use it. Fortunately, Javascript comes with just such a tool: [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse).

Currently, the code to parse the JSON looks like this:

```
var data = eval('('+xhr.responseText+')');
```

Fixing it is basically a single line replacement. Update the code to use this instead:

```
var data = JSON.parse(xhr.responseText);
```

This takes in the same string as before but passes it through a more robust and tested parser and puts the object structure into the `data` variable. All values are accessible exactly as they were before and there's no risk of Javascript being evaluated during the JSON decoding process.

Now, even if you have a left-over `alert(1)` in your JSON, you'll no longer receive the popup message when the user list loads.

> One thing to note here is that, if your JSON does have an invalid JSON element in it (like `"id":alert(1)`) you'll receive an error using `JSON.parse` in the browser console for an "unexpected token". This is yet another preventative control, reducing risk from JSON documents with poor structure.