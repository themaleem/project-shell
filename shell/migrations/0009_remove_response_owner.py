# Generated by Django 3.0.5 on 2020-04-14 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0008_response_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='owner',
        ),
    ]