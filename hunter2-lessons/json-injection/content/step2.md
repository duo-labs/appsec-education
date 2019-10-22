# Handling JSON

With some of the basics of JSON out of the way, we can move on to the next step in the use of a JSON document: parsing. JSON was developed with a consistent structure specifically so it would be easier for systems to exchange information in an easy-to-parse manner. 

Over the years the structure of JSON has stayed largely the same but there have been countless numbers of JSON parsers created is a wide range of languages. Some of these are built into the languages themselves including:

- Python's [native JSON functionality](https://docs.python.org/3/library/json.html)
- PHP's [JSON handling](http://php.net/manual/en/book.json.php)
- the Java [org.json package](https://github.com/stleary/JSON-java)
- Go's [encoding/json package](https://gobyexample.com/json)

These usually include just the basics of parsing JSON content. Third-party packages often overlay on this functionality and provide other convenience functionality.

In this application, however, the developer chose to implement their own JSON parsing engine making use of regular expressions and manual read/write functionality instead of a built-in library. Much like with other practices in development, "rolling your own" should only be an option if there's not already something included (or battle tested) for the language. Many vulnerabilities can be introduced in the creation of a parser without the developer even knowing.

To see how our application is reading and writing JSON, open the `app.py` file and look for the `parseJson` and `writeJson` methods near the bottom of the file.

```
pico app.py
```
