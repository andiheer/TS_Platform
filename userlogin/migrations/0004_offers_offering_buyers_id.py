# Generated by Django 2.2.2 on 2019-07-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0003_offers_offering_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='offering_buyers_id',
            field=models.IntegerField(default=0),
        ),
    ]
