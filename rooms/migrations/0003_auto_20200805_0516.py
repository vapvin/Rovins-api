# Generated by Django 3.1 on 2020-08-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20191216_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-pk']},
        ),
    ]
