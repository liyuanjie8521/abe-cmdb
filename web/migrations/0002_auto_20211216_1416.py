# Generated by Django 3.1 on 2021-12-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(db_index=True, max_length=32, verbose_name='用户'),
        ),
    ]
