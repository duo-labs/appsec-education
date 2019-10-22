# Using the "Users" API

### An Overview

Before we get into describing and exploiting the vulnerabilities we're going to talk about related to JWTs, lets make sure that it's understood how to use our "Users" API. As you can see from [the documentation]({$VIRTUAL_HOST}), there are two different endpoints: the `/login` endpoint and a `/users` endpoint. 

### Logging In

The first endpoint - `/login` - is used to authenticate your user in the system. In this system we've already set up some users for you so you don't have to worry about creating your own:

```
username: user1, password: test1234
username: user2, password: test5678
```

Send a `POST` request to the `/login` endpoint with this data:

```
username=user1&password=test1234
```

This will successfully log you in and return a message with a `message` that contains a `token` value. This is your JWT token to use for the other requests.

### Making a request for users

Now that we have a token, we can make a request to get the users in the system. As the documentation notes, if your user doesn't have admin level access, you will only receive your own information. Both of our pre-defined users only have "user" level access so they'll only get their own details.

This request requires you to be authorized so we need to include the token we just received in the `X-Auth-Token` header. Make a `GET` request to `{$VIRTUAL_HOST}/users` including this header value to return the user information. With `curl` it might look like this:

```
curl --request GET --url {$VIRTUAL_HOST}/users \
  --header 'X-Auth-Token: [token goes here]'
```

Now that we know how to use the API the right way, lets see how we can abuse the JWT token and try to bypass it and elevate our privilege.
