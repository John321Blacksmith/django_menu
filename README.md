# django_menu

In sake of brevity, this django app allows you to create a menu in a particular HTML template.
The menu is created with a unique name based on the 'slug' value specified when defining a new **Menu** model on the Django-admin toolpage.
There are several expanded layers in the tree menu. The *first layer* is a block of the parental menus, ones that are added via the 'slugs'. 
The *second one* contains all the menu entities each **menu** may contain. The *last layer* comprises of sub-entities each **menu entity** contains.
An entire menu system is stored in the DataBase. All the levels of menu are either modified or deleted via the Django-admin toolpage.
