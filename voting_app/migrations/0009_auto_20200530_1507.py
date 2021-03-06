# Generated by Django 3.0.6 on 2020-05-30 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting_app', '0008_auto_20200530_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='hosted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='options',
            name='event_code',
            field=models.CharField(max_length=200),
        ),
    ]
