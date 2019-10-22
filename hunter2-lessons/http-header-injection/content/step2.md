# What is header injection?

#### How are headers used?

Before we can talk about header injection, we need to talk about some common HTTP headers. Here's just some of the headers that could be a part of an HTTP request (full listing can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)):

- Host
- Cookie
- Authorization
- Access-Control-Allow-Origin
- Location

Many of the headers in a typical HTTP request include piece of user content. This includes headers like `Cookie` and `User-Agent`. As with the security in many other parts of a web-based application, any place where user input can be used in output has the potential for creating a vulnerability and HTTP headers are no exception.

#### How header injection attacks work

Header injection happens when unfiltered and unvalidated user input is allowed into the HTTP header response information. This allows a user to input any values directly into the response, allowing them direct control over what is sent back to the user.

- Truncating response data by modifying the content length
- Disabling XSS protection
- Spoofing "forwarded for" headers used by many proxies

With the [wide range of HTTP headers available](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) there's too many possible exploits to list out here, but from these examples alone you can get an idea of how dangerous header injection could be.