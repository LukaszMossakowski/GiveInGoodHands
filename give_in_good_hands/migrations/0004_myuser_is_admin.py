# Generated by Django 3.1.1 on 2020-09-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('give_in_good_hands', '0003_auto_20200911_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
