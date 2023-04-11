# CA4 - BACK END DEVELOPMENT #
## Flask To-Do Application## ##
### Lucas Bandeira - 23884 ###

This is a to-do flask application connected with MongoDB, and flask user authentication. In order to run this application, you will have to install the following libraries

- pip install flask pymongo flask-login

The user should be able to login or register in the application. 
They will also be able to create and delete to-do tasks. 
These tasks will then be stored in a MongoDB cloud environment managed by the admin.

Below you can see a screenshot of the home page of this application.

![img.png](images/img.png)

The user can then create an account within the application. It is important
to mention that the to-do object will only be sent to the database if they are bound to a user account.

![img_1.png](images/img_1.png)

In case the user still has not created an account he can then navigate to route register.

![img_2.png](images/img_2.png)

Once they are registered and logged in. The user will be able to create and delete to-do tasks.

![img_3.png](images/img_3.png)

The user data is kept in the MongoDB along with his to-do tasks history.

![img_4.png](images/img_4.png)

As you may have noticed the password is encrypted for security purposes.

![img_5.png](images/img_5.png)


## References ##

- SSL Certificate for MacOS - https://pymongo.readthedocs.io/en/stable/examples/tls.html
- Flask and MongoDB tutorial - https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
- Flask Login - https://www.youtube.com/watch?v=71EU8gnZqZQ&t=585s
