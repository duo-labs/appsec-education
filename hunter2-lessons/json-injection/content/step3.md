# Reconnaissance

First, before we can try to exploit our application, we need to do a little reconnaissance work. Knowing the process of how to find this issue is just as important as fixing it. 

Lets start with the main page. Go to your application in a browser and you'll be given a simple page with a listing of users in a table. If you view the source of the page, you'll see that this table is populated by an AJAX call to the `/user` endpoint. If you visit this endpoint in your browser, you'll be given the current JSON structure for the user list.

When the `Edit` link is clicked for the user, their information is populated into the form from the `/user/[id]` endpoint. When `Save User` is clicked, the `/save` endpoint is called (via a `POST` request type) to update the information. If the user doesn't already exist, they'll be created as a new record and added to the JSON. This is the basic functionality of the page.

### Trying to break it

Get out your "unofficial pentester" hat because we're going to try and break the application in its current state. Don't worry, you can always click `Reset Users` to reset the data to a fresh state. Here's some things to try:

- Put values other than just a username or email address into the fields (like quotes or other special characters)
- Try an XSS attack using `<script>alert(1)</script>`
- Break the JSON by using JSON-specific characters like curly braces and colons

If you try these kinds of attacks, you'll notice that - more than likely - you'll have broken the JSON so the table is no longer populated. This is because of how our custom JSON parser works and the result it outputs. But we're trying to do something we can use here, not just break things, so we need to figure out another path forward.

Are there other values that maybe we could try using in the JSON document...?