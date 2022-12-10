# finally-assesment

**Instructions:**

We need to setup the database, install the dependencies and run the django application.

**_Setting up the database:_**

The database name , username and password can be set up in backend/ settings.py file at lines 144 to 146
![image](https://user-images.githubusercontent.com/78776401/206827517-9af5d745-4c7f-4e08-959b-5113e7d7d192.png)

**_Installing dependencies:_**

1. Go to the folder that contains requirements.txt and use the below command to install all the used dependencies:

```
$ pip install -r requirements.txt
```

2. To run the server, cd to the directory that has manage.py and execute the below command in bash:

```
$ python manage.py runserver
```

**_Create a superuser with the below comand, the email should be the username:_**

```
$ python manage.py createsuperuser
```

**_Login to the admin panel using the superuser credentials at (The email is the username):_**

```
http://127.0.0.1:8000/admin/
```

**_Now that everything is set up, you can use the backend api's using postman._**

**Documentations can be found at**

1. Postman:

```
https://documenter.getpostman.com/view/22813960/2s8YzTSgwS
```

2. Swagger:

```
http://127.0.0.1:8000/swagger/
```

3. ReDoc

```
http://127.0.0.1:8000/redoc/
```
