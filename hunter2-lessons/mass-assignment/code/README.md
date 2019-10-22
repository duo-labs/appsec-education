# Lab: Mass assignment

## General Information

- was brought into light as a major issue with Rails 
- even GitHub was hacked because of it

- to fix, requires mass assignment to be prevented by default
    This means defining the properties that are allowed to be filled via configuration

- Not just rails was/is vulnerable
    It happens because values are used directly without being checked or filtered
    It needs to be enabled by default, not just as an option. If default allows it, 
    it leads to vulnerabilities

-----------
> On Sunday morning, 4 March [2012], Egor Homakov exploited a flaw in how the Ruby on Rails web framework
> handles mass assignments that allowed him to write a posting, delete a posting or push changes into
> source code on any GitHub project. Homakov had previously created an issue regarding mass
> assignment security on the rails issue tracker on GitHub; this was closed by the developers saying
> that it was the application developers' responsibility to secure their applications. Homakov then 
> decided to demonstrate the issue using the nearest Ruby on Rails application, GitHub.

> He first created an issue on the Rails project's issues list timestamped 1001 years into the future,
> to get the attention of the Rails developers. Then, he added his public key to the list of Rails 
> committers and made a commit to the Rails master repository. GitHub suspended Homakov's account, 
> while they fixed the problem. After GitHub fixed the issue, Homakov published a how-to on how he 
> had manipulated GitHub's Rails applications.
-----------

## Outline

1. Talk about the history of the vulnerability and why it's a problem
2. Present the code example and cover how it works to take in the user add and update
3. Define where the issue is and how it is happening (the push of all data into the JSON for saving without any kind of validation or filtering)
4. Show how to exploit it with a custom `curl` command copied from the browser developer tools (or manually created) and updated to send the `username` value
5. Fixing the issue with several different methods:
    - performing validation on the input to make sure the `username` value isn't a part of the update data
    - updating only certain values and not the entire object
6. Also provide an example of a tool that only allows updates on certain properties defined as "fillable"

## Resources

- [OWASP Mass Assignment Cheatsheet](https://www.owasp.org/index.php/Mass_Assignment_Cheat_Sheet)
- [Wikipedia entry](https://en.wikipedia.org/wiki/Mass_assignment_vulnerability)
- [Exploring Rails Mass Assignment Vulnerability](https://medium.com/@jaeger.rob/exploring-rails-mass-assignment-vulnerability-b8b3d19e20b6)
- [Acunetix: Rails mass assignment](https://www.acunetix.com/vulnerabilities/web/rails-mass-assignment/)
- [Mass Assignment Vulnerability: Secure Your Rails Apps!](https://pragtob.wordpress.com/tag/mass-assignment-vulnerability/)
- [relevant GitHub scurity issue](http://www.h-online.com/open/news/item/GitHub-security-incident-highlights-Ruby-on-Rails-problem-1463207.html)

- [Original issue posted to the Rails project](https://github.com/rails/rails/issues/5228)

- [Building a REST API with Flask and the Orator ORM](http://blog.eustace.io/buiding-rest-api-with-flask-orator.html)

## To build locally via Docker Compose:

```
docker-compose up
```

Then, to correctly build and see the `/tmp/test.db` SQLite database:

```
cd /app
python cli.py migrate:refresh -f --seed
```
