# Generated by Django 3.2.4 on 2021-07-05 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
