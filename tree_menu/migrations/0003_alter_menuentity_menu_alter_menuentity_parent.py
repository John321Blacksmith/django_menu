# Generated by Django 4.1.7 on 2023-03-01 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_alter_menuentity_menu_alter_menuentity_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuentity',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menuentity', verbose_name='menu'),
        ),
        migrations.AlterField(
            model_name='menuentity',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.menu', verbose_name='parent'),
        ),
    ]
