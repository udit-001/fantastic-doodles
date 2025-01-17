# Generated by Django 3.2.12 on 2022-02-28 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VideoResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('thumbnail_url', models.URLField()),
                ('published_on', models.DateTimeField()),
                ('query', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='videos.searchquery')),
            ],
        ),
    ]
