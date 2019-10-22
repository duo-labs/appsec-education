# Lab: HTML Injection

## Outline

- What are HTTP headers?
- What is header injection?
- Exploit example: a URL parameter that’s mirrored directly in the response. This would allow them to inject URL encoded newlines and put in any other header they’d like.
- Correcting the issue: either removing the input from the headers or using a method that prevents the injection (escaping?)

This requires familiarity with the use of browser developer tools to view the HTTP headers.

## Resources

- [Graceful Security: HTTP Header Injection](https://www.gracefulsecurity.com/http-header-injection/)
- [Netsparker: CRLF, HTTP Response Splitting & HTTP Header Injection](https://www.gracefulsecurity.com/http-header-injection/)
- [PortSwigger: HTTP response header injection](https://www.gracefulsecurity.com/http-header-injection/)
- [Mozilla: HTTP header reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

## To build locally via Docker Compose:

```
docker-compose up
```

## Example Headers to Try

The header injection allows you to put any header you'd like in the page but here are some interesting ones.

```
X-Foo: bar
Set-Cookie: test=1234
Refresh: 0; url=http://duo.com
```