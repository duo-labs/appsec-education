# What is a Replay Attack?

### HTTP Request Handling

In order to understand what replay attacks are, you need to understand a bit about how HTTP requests are made. Normal HTTP requests (not HTTPS) are just plain-text messages structured in a pre-defined format that both the client and the server know how to "speak". These HTTP requests include several sections including:

- header information (metadata about the request)
- body content
- resource (URL) to access
- version of the HTTP protocol to use

For every HTTP request made from a client to the server - be it a normal user's browser or an attacker's malicious script - the structure stays the same with only the values changing from request to request.

Because HTTP requests are "stateless" each request is isolated and it's up to the server to persist any data that might be needed between requests. This statelessness and consistent structure make it easy to capture these requests as they go between client and server and repeat them as often as desired.

When this repeating is used maliciously, it's called a "replay attack".

### An Example

Imagine a banking application that allows you to make "transfer" requests via their web application. In thi request you would define a "to" account and an "amount" value. Our HTTP request might look something like this:

```
POST /transfer HTTP/1.1
Host: mybank.com
Session: c06db68e819be6ec3d26c6038d8e8d1f

to=1234567890&amount=1000.00
```

The server would then process this request and pull the $1000.00 from the user's account and transfer it over to the `1234567890` account. However, if an attacker were able to intercept this (using a man-in-the-middle attack of some kind), there's nothing preventing them from taking this same request, updating the `to` account number and sending it to the server as many times as they'd like.

Try and make requests to the `{$VIRTUAL_HOST}/transfer` endpoint, changing the account number to `1111111111` and see how much you can transfer over.
