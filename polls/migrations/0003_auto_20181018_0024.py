# Generated by Django 2.1.1 on 2018-10-18 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181017_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Choice_text',
            new_name='choice_text',
        ),
    ]
