# Summary

In this lesson we've walked through what HTTP headers are and how, when tainted data makes its way into them, bad things can happen. This lesson just scratched the surface on what could be done with an HTTP header injection. There's a [whole world of other HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) that could be injected to perform other types of attacks without the knowledge of the user, including potentially overriding current headers.

In most languages, the HTTP headers are parsed "last in wins", only allowing for one value. This means that if you had one `X-XSS-Protection` header that enforced browser-based [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) protection and overrode it with `X-XSS-Protection: 0`, an XSS issue on the page might suddenly work.

So, to wrap up, here's a few general recommendations when it comes to using dynamic HTTP headers in your application:

1. Never use user input as a part of a header if possible.
2. Always opt for using built-in tooling from your framework or library rather than rolling your own
3. If you have to do it manually, ensure that any user input is stripped of newline characters