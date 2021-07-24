# Generated by Django 3.2.4 on 2021-07-13 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210713_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='other_name',
        ),
        migrations.AddField(
            model_name='students',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user'),
            preserve_default=False,
        ),
    ]
