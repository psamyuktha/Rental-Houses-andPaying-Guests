# Generated by Django 2.1.3 on 2018-12-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_pages2', '0007_auto_20181208_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='gallery',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='gallery1',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='house',
            name='gallery2',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
