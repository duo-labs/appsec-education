# What are HTTP headers?

HTTP (Hypertext Transfer Protocol) was originally developed by a team headed by Tim Berners-Lee at CERN in 1989. It was overseen by several major web standards groups including the IETF and W3C. The team created the initial version of the HTTP specification, HTTP/1.0, which was later improved upon in 1997 with the introduction of HTTP/1.1. Several other smaller changes have been added since then but the main structure of HTTP requests has remained the same.

HTTP make use of a request and response model with well-defined structures for both types of messages. The end user/client makes the request using one format and, using a similar format, responds with content based on the resource requested.

Here's an example of a basic HTTP request for the index document of a server:

#### Request
```
GET / HTTP/1.1
Host: myserver.com
```
#### Response
```
HTTP/1.1 200 OK
Host: myserver.com

<html><body>This is the index page</body></html>
```

In the example above, the client makes the request to the `myserver.com` host for the `/` (index) document. The server then responds with a `200 OK` message indicating the resource was found and returns the content for the resource (the HTML markup). The section above the content are the HTTP headers. This information can be thought of as "metadata" for the request/response and provides some key information to the client about the content and request.

The application we'll be using in this lesson should boot up automatically and give you the URL where it can be accessed. If it does not, type `boot` and hit return to manually start the application.

## Check
`cat /var/log/nginx/access.log | grep 'GET / HTTP/1\.1\" 200 ' | wc -l | { [[ $(cat) -ge 1 ]] && echo yes; }`