# Generated by Django 2.1.3 on 2018-12-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_pages2', '0004_delete_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='amenities',
            field=models.ManyToManyField(to='client_pages2.Amenities'),
        ),
    ]