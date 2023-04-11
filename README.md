# CA4 - BACK END DEVELOPMENT #
## Flask To-Do Application## ##
### Lucas Bandeira - 23884 ###

This is a to-do flask application connected with MongoDB, and flask user authentication. In order to run this application, you will have to install the following libraries

- pip install flask pymongo flask-login

### Run through video ###
- https://youtu.be/fAtQuYsW3ng

The user should be able to login or register in the application. 
They will also be able to create and delete to-do tasks. 
These tasks will then be stored in a MongoDB cloud environment managed by the admin. It is important
to mention that the to-do object will only be sent to the database if they are bound to a user account.

In case the user still has not created an account he can then navigate to route register.
Once they are registered and logged in. The user will be able to create and delete to-do tasks.
The user data is kept in the MongoDB along with his to-do tasks history. As you may have noticed the password is encrypted for security purposes.



## References ##

- SSL Certificate for MacOS - https://pymongo.readthedocs.io/en/stable/examples/tls.html
- Flask and MongoDB tutorial - https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
- Flask Login - https://www.youtube.com/watch?v=71EU8gnZqZQ&t=585s
