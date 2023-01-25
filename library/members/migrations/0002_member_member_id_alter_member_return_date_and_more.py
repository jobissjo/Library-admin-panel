# Generated by Django 4.1.4 on 2023-01-02 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.CharField(default=datetime.datetime(2023, 1, 2, 12, 27, 49, 631478, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='taken_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]