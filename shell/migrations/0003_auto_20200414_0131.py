# Generated by Django 3.0.5 on 2020-04-14 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0002_auto_20200414_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile'},
        ),
        migrations.AlterField(
            model_name='draft',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]