# Generated by Django 2.1.3 on 2018-12-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_pages2', '0005_detail_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='gallery',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='house',
            name='gallery1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='house',
            name='gallery2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
