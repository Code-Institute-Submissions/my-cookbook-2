# Generated by Django 3.2.15 on 2022-09-13 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_posted']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='date_posted',
        ),
    ]
