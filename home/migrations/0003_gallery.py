# Generated by Django 3.2.4 on 2021-11-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_team_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
