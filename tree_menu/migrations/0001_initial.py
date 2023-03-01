# Generated by Django 4.1.7 on 2023-03-01 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existence', models.BooleanField(default=True, verbose_name='visibility')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', models.SlugField(help_text='Use this snippet along with a template tag as a name of the rendered menu', max_length=255, unique=True, verbose_name='slug')),
                ('named_url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existence', models.BooleanField(default=True, verbose_name='visibility')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('named_url', models.CharField(blank=True, max_length=255, verbose_name='url pattern')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menu')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menuentity')),
            ],
            options={
                'verbose_name': 'menu title',
                'verbose_name_plural': 'menu titles',
            },
        ),
    ]