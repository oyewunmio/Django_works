# Generated by Django 3.2.4 on 2021-07-10 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='File',
            field=models.FileField(blank=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]