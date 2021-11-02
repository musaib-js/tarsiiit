# Generated by Django 3.2.4 on 2021-10-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
                ('desc', models.TextField()),
                ('fb_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('googleplus_link', models.URLField()),
            ],
        ),
    ]