# Generated by Django 3.2.4 on 2021-07-24 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210724_1453'),
        ('classes', '0002_rename_subjects_classes_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='Teachers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]