# Generated by Django 3.2.4 on 2021-07-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('PARENT', 'Parent')], default='STUDENT', max_length=50, verbose_name='Type'),
        ),
    ]