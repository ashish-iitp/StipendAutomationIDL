# Generated by Django 4.0.1 on 2022-03-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bank_account',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='project',
            field=models.IntegerField(default=0),
        ),
    ]
