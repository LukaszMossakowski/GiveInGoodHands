# Generated by Django 3.1.1 on 2020-09-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('give_in_good_hands', '0006_donation_is_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.CharField(blank=True, choices=[('taken', 'zabrane'), ('not_taken', 'niezabrane')], default='not_taken', max_length=64),
        ),
    ]
