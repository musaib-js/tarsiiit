# Generated by Django 3.2.4 on 2021-11-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
