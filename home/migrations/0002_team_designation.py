# Generated by Django 3.2.4 on 2021-11-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='designation',
            field=models.CharField(default='', max_length=200),
        ),
    ]
