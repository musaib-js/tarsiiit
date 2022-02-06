# Generated by Django 3.2.4 on 2022-02-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=245)),
                ('subject', models.CharField(max_length=240)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment_Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('college_id', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=12)),
                ('proposal', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Recruitment Queries',
            },
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Gallery'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Team'},
        ),
    ]