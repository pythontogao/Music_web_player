# Generated by Django 2.1.1 on 2018-11-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181028_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]