# Generated by Django 3.2.8 on 2021-11-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_comment', models.TextField()),
                ('miss', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]