# Generated by Django 3.1.1 on 2022-03-29 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20220329_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='winings', to=settings.AUTH_USER_MODEL),
        ),
    ]