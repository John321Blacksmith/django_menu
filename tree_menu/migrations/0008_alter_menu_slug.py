# Generated by Django 4.1.7 on 2023-03-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0007_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(help_text='Use this snippet along with a template tag as a name of the rendered menu', max_length=255, verbose_name='slug'),
        ),
    ]
