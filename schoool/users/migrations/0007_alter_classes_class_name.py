# Generated by Django 3.2.4 on 2021-07-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210721_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='Class_name',
            field=models.CharField(max_length=10),
        ),
    ]