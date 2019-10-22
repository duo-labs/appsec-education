# Why Does a Replay Attack Work?

### Repetition and State

In the previous step, we made an example request to the `/transfer` endpoint to see just how much money we could pull out of the user's account and into ours. If you kept trying long enough (or transferred a large enough amount) you'd drain their account and end up with an error if no more funds could be moved.

But why does this work? If you're not the user, how can you make a request from a completely different place and have the transfer still work? The key is in the header information, specifically the `Session` header. This is a clue that the application is persisting something on the server and using this to relate the requests and maintain some kind of state. We, as the attacker, intercepted this message and ran a quick test to see if any errors popped up when we did. In our example, no other checks are done besides relating the request to the session so we were allowed to transfer the funds without question.

### Exploiting the Hole

As you may have guessed, the main reason that replay attacks work is the lack of other security controls on the request. In our `/transfer` example, the only security control that was in place was the `Session` ID value. The application assumes that the presence of this value and its relation to a currently active session mean that the user has already passed another security control, most likely a login of some kind.

Many attackers, however, don't need to try and break down the front door when they can sneak in through a hole in the fence. In this case, that "hole" is their interception and re-use of the same HTTP request without needing to bypass the login themselves.

Now we'll take a look at a more realistic example application that's still vulnerable to a replay attack: a user management API. This application will have the same basic flaw as our `/transfer` endpoint but it will be a bit more tricky to exploit.

The main code for this API is in `app.py`. Go ahead and open that file in an editor now.
