# Generated by Django 4.2.5 on 2023-11-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_repository_folder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='Owner',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
