# Generated by Django 2.0.7 on 2018-07-25 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_added',
        ),
    ]