# Generated by Django 2.0.5 on 2018-07-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0017_auto_20180507_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='user',
        ),
        migrations.AddField(
            model_name='candidate',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='candidate',
            name='label',
            field=models.TextField(default=''),
        ),
    ]
