# Generated by Django 3.0.5 on 2020-04-15 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_username', models.CharField(max_length=20)),
                ('status', models.TextField(blank=True, default='Love and Light!', max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avis/')),
                ('one_word_description', models.CharField(max_length=15)),
                ('bio', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
