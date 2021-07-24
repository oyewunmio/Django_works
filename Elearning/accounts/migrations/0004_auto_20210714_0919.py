# Generated by Django 3.2.4 on 2021-07-14 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('accounts', '0003_auto_20210714_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.school_class'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='Class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.school_class'),
        ),
    ]
