# Generated by Django 2.2.10 on 2020-03-15 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionadmin', '0002_auto_20200315_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('order', 'questiontype')},
        ),
    ]
