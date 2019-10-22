# The Application & Adding Users

Our application performs some pretty basic user handling. The main page lists out several users in the system and their details. You can also use the "pencil" icon on their record to update their information or use the "Add New User" form to add a new one.

In the main `app.py` file, there are four routes defined: a `GET` and `POST` for the main page and a `GET` and `POST` for the user edit page. The `POST` handler for the main page is what takes in the details from the "Add New User" form and the `POST` for the edit page updates the values for a current user. All functionality makes use of a `userManager` object and its methods to create and save the users.

By default our application has a `userManager` that makes use of flat files on the local file system that contain JSON data. You can see this structure in the `data/users.json` file. Each user record contains a username, name, email and password records (as well as a unique ID). 

Use the "Add a New User" form and create a new user. Then look at the changes in the `data/users.json` file for the new addition. In our application, this incoming data is passed off to the `userManager.addUser` method for handling.

Let's see what this is doing. According to our `import` lines at the top of the `app.py` file, we're importing the `user_json` module as the manager. Open this file and locate the code for the `addUser` method. Adding a new user is a pretty simple operation with Python's `json` handling - the JSON file is parsed and a the data for the new user is pushed into the set using the `append` method. The resulting data is then written back out.

In its current state, the `POST` endpoint for adding a new user takes all of the values provided from the "Add New User" form request and pushes it into the JSON. This seems fine and seems to work securely. 

Now lets move on to updating a user's information and see if there's any issues there.
