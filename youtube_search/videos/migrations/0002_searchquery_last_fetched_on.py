# Generated by Django 3.2.12 on 2022-02-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='last_fetched_on',
            field=models.DateTimeField(null=True),
        ),
    ]
