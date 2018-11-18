# Generated by Django 2.1.2 on 2018-11-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181117_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_hostel',
            name='bed_type',
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='double_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='double_wa',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='single_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='single_wa',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='triple_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='triple_wa',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Bed_Type',
        ),
    ]
