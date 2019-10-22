# The Basics of JSON

### Origins

When (JSON](https://www.json.org/) (Javascript Object Notation) was proposed back in December of 1999, it was promoted as an another option to use besides XML (which had been made a de-facto document structure format a few years prior) for data storage formatting. JSON was originally developed out of the need for something more lightweight than XML or other more complex formats and was based around a language structure that already existed: Javascript.

It's goal was to be both easy for humans to be able to follow and still structured enough for systems to be able to parse it without supervision via automated parsers.

### Common Uses

Since its definition JSON has enjoyed use in a wide range of applications and, because of its simplicity, has becoming one of the default formats for many APIs. In most cases, the information shared between the client using the API and the server can be expressed using JSON's formatting. There are more complex cases that might require the use of XML, but often times JSON's simplicity is enough.

Besides use in APIs, JSON is also used several database systems as a native data storage method such as [MongoDB](https://www.mongodb.com/) (NoSQL) and MySQL via its [JSON data type](https://dev.mysql.com/doc/refman/8.0/en/json.html).

### Example Structure

Our application is going to make use of a simple JSON document stored on the file system: `data/users.json`. You can see the contents of this file and its structure using this command:

```
cat data/users.json
```

This document is storing the user data - `email` and `username` - that our application will use.