# Generated by Django 4.0.1 on 2022-04-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rndadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rndadmin',
            old_name='passwd',
            new_name='password',
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='null', max_length=30),
            preserve_default=False,
        ),
    ]