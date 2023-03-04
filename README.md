# django_menu

In sake of brevity, this django app allows you to create a menu in a particular HTML template.
The menu is created with a unique name based on the 'slug' value specified when defining a new **Menu** model on the Django-admin toolpage.
There are several expanded layers in the tree menu. The *first layer* is a block of the parental menus, ones that are added via the 'slugs'. 
The *second one* contains all the menu entities each **menu** may contain. The *last layer* comprises of sub-entities each **menu entity** contains.
An entire menu system is stored in the DataBase. All the levels of menu are either modified or deleted via the Django-admin toolpage.

# Setting up
1) Assuming you've got the latest version of Django and everything based on the requirements.txt is ready to use, set up a superuser account:
```
python manage.py createsuperuser
```
2) Then create a blank pythonic file and name it, say, **secrs.py** where you should store your Django SECRET KEY, your admin-password and username;
3) In settings.py, if you are up to, besides your SECRET KEY, you can retrive all the private data and locate it in the **secrs.py**. So you can further import this file to **settings.py** and substantiate all the retrived data by just the imported variables. Note that the file with your credentials should be located in the *same* directory as the **settings.py** file is. Otherwise, you will have to change a system path in working program;
4) Run the server and go to the admin page;
