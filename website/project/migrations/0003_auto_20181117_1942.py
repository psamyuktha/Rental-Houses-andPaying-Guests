# Generated by Django 2.1.2 on 2018-11-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20181117_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_hostel',
            name='Feedback',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='Rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]