# Generated by Django 3.2.4 on 2021-07-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_students_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='Class',
        ),
    ]
