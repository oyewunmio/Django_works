# Generated by Django 3.2.4 on 2021-07-24 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_remove_classes_teachers'),
        ('users', '0004_auto_20210724_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermore',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.classes'),
        ),
    ]
