## Introduction

In our sample application, we’ve set up a common scenario: a user arrives at an application and in order to use the service, they need to create a login. Once they’ve registered they can then log in to the application and begin to use the service. 

In the case of our application, however, a secondary code (uniquely and randomly generated) is provided that they must use to complete the login process. When this code and the username are entered, the two are verified and - if successful - the user login process is complete.

Ideally this code would be sent via a second factor (such as an SMS message) but our application operates in isolation so the code is provided during the login flow.

### To continue

To begin, type `boot` to start the server, then visit the URL for your app.
