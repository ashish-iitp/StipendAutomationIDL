# Generated by Django 4.0.1 on 2022-05-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_employee_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='professors',
            field=models.CharField(choices=[('test1@gmail.com', 'test1@gmail.com'), ('test2@gmail.com', 'test2@gmail.com'), ('test3@gmail.com', 'test3@gmail.com'), ('test4@gmail.com', 'test4@gmail.com')], max_length=50),
        ),
    ]