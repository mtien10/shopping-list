# Generated by Django 3.2.9 on 2021-12-14 14:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0002_shoppingitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='share_users',
            field=models.ManyToManyField(related_name='share_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
