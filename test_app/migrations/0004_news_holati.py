# Generated by Django 4.2.4 on 2023-09-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='holati',
            field=models.BooleanField(default=True),
        ),
    ]
