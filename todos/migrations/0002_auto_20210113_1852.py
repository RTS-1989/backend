# Generated by Django 2.2.6 on 2021-01-13 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='book',
            new_name='body',
        ),
    ]
