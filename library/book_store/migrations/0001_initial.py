# Generated by Django 4.1.4 on 2022-12-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=1)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available'), ('Comming Soon', 'Comming Soon')], max_length=50)),
            ],
        ),
    ]
