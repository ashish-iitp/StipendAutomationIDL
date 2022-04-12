# Generated by Django 4.0.1 on 2022-03-21 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.IntegerField(max_length=5)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bank_account', models.IntegerField(max_length=20)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('hire_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
    ]