# Generated by Django 3.2.4 on 2021-07-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Isbn_no', models.CharField(max_length=100)),
            ],
        ),
    ]