# Generated by Django 3.2.4 on 2021-07-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_teachers_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
        migrations.AddField(
            model_name='students',
            name='picture',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='teachers',
            name='picture',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]