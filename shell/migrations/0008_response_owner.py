# Generated by Django 3.0.5 on 2020-04-14 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shell', '0007_remove_response_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='owner',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
