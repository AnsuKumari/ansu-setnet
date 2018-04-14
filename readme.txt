SETNET Project
-------------------------------------------------
Setnet is a Django 2.0 web project that provides its user with basic social networking site functionality.



Prerequisites
-------------------------------------------------
Be sure you have the following installed on your development machine:

    Python >= 3.6
    Postgres >= 9.2
    
(In case you are unable to work with PostgreSQL you can use Sqlite3. Sqlite3 is a lightweight database that comes with python. No extra module needs to be downloaded.)



Configuring database
-------------------------------------------------
For PostgreSQL:
Create databse user and databse with following values to use for development.

    database user : root
    password : root
    database : setnet

Ensure that the default DATABASES url string in setnet/settings.py corresponds to your database.


For Sqlite3:
Change the DATABASES url string in setnet/settings.py to the following.

*********** FROM ***********
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'setnet',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}

*********** TO *************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'setnet.sqlite3',
    }
}



Quickstart
-------------------------------------------------
1. Install development dependencies,
    pip install -r requirements.txt
    
2. Setup database tables,
    python manage.py migrate # create neccessary tables
    
3. Run the web application locally,
    python manage.py runserver # localhost:8000/ or 127.0.0.1:8000/



Urls
-------------------------------------------------
1. Home page : /

2. Admin page : /admin/

3. Create User : /accounts/register/

4. View User : /accounts/profile/<profile_id>

5. Edit User : /accounts/profile/<profile_id>/edit

6. Login User : /accounts/login/

7. Logout User : /accounts/logout/

8. Create post : post/new/

9. View post : post/<post_id>

10. Edit post : post/<post_id>/edit/

11. Delete post : post/<post_id>/remove/

12. Add comment : post/<post_id>/comment/

13. Delete comment : comment/<comment_id>/remove/
