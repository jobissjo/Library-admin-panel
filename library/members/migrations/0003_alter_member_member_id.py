# Generated by Django 4.1.4 on 2023-01-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_member_id_alter_member_return_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.CharField(max_length=15),
        ),
    ]