# Exploiting HTTP Headers

For our example, we're going to use a simple vulnerable script based on the Python [Flask framework](http://flask.pocoo.org/) that makes it easy to handle incoming HTTP requests and send back the appropriate HTTP responses. 

We're going to start with a vulnerable page so you can see the exploit in action. Navigate to your application by visiting this URL in your browser:

```
http://$VIRTUAL_HOST/vulnerable
```

You'll see in the plain-text response that there's an error. A `username` value seems to be missing from the request. This is our first clue as it provides a way to input user-defined content into the system. In this case, it's looking for a `username` value on the `GET` request so see what happens using this URL: `http://$VIRTUAL_HOST/vulnerable?username=test`. 

If you look at the HTTP headers of the response (either using something like `curl` or the Developer Tools in your browser) you can see that there's a special header set - `X-Username` - with the value you provided. This is another hint that there might be something that could be abused here.

HTTP headers make use of newlines to separate them so in order to perform the injection, we need to figure out how to get a newline into that user input (the username). Since the `username` value is on the URL, we need to URL encode the newline to `%0A`. This will inject the newline after the username value and we can trick the browser into injecting the new header value. Visit this URL and see what happens:

```
http://$VIRTUAL_HOST/vulnerable?username=test%0AX-Exploited:%20123
```

If you look in the headers for the response, you should now see the `X-Exploited` header included in the list as a valid header!


## Check
`cat /var/log/nginx/access.log | grep 'GET /vulnerable?username=test%0AX-Exploited:%20123 HTTP/1\.1\" 200 ' | wc -l | { [[ $(cat) -ge 1 ]] && echo yes; }`