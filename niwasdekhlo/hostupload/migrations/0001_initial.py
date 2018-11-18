# Generated by Django 2.1.2 on 2018-11-18 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('am_id', models.AutoField(primary_key=True, serialize=False)),
                ('amenities', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bed_Type',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('bed_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('single_a', models.IntegerField(null=True)),
                ('single_wa', models.IntegerField(null=True)),
                ('double_a', models.IntegerField(null=True)),
                ('double_wa', models.IntegerField(null=True)),
                ('triple_a', models.IntegerField(null=True)),
                ('triple_wa', models.IntegerField(null=True)),
                ('four_a', models.IntegerField(null=True)),
                ('four_wa', models.IntegerField(null=True)),
                ('price_paid', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('status', models.IntegerField()),
                ('Feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking_House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('single_a', models.IntegerField()),
                ('single_wa', models.IntegerField()),
                ('double_a', models.IntegerField()),
                ('double_wa', models.IntegerField()),
                ('triple_a', models.IntegerField()),
                ('triple_wa', models.IntegerField()),
                ('floorbed', models.IntegerField()),
                ('price_paid', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('status', models.IntegerField()),
                ('Feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_a', models.IntegerField()),
                ('single_wa', models.IntegerField()),
                ('double_a', models.IntegerField()),
                ('double_wa', models.IntegerField()),
                ('triple_a', models.IntegerField()),
                ('triple_wa', models.IntegerField()),
                ('four_a', models.IntegerField()),
                ('four_wa', models.IntegerField()),
                ('avg_rating', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('gallery', models.URLField(null=True)),
                ('amenities', models.ManyToManyField(to='hostupload.Amenities')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_a', models.IntegerField()),
                ('single_wa', models.IntegerField()),
                ('double_a', models.IntegerField()),
                ('double_wa', models.IntegerField()),
                ('triple_a', models.IntegerField()),
                ('triple_wa', models.IntegerField()),
                ('floorbed', models.IntegerField()),
                ('avg_rating', models.IntegerField()),
                ('description', models.TextField()),
                ('gallery', models.URLField()),
                ('guest', models.IntegerField()),
                ('amenities', models.ManyToManyField(to='hostupload.Amenities')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing_Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_a', models.IntegerField()),
                ('single_wa', models.IntegerField()),
                ('double_a', models.IntegerField()),
                ('double_wa', models.IntegerField()),
                ('triple_a', models.IntegerField()),
                ('triple_wa', models.IntegerField()),
                ('four_a', models.IntegerField()),
                ('four_wa', models.IntegerField()),
                ('cleaning', models.IntegerField()),
                ('security', models.IntegerField()),
                ('cab', models.IntegerField()),
                ('food', models.IntegerField()),
                ('extra', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing_House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_a', models.IntegerField()),
                ('single_wa', models.IntegerField()),
                ('double_a', models.IntegerField()),
                ('double_wa', models.IntegerField()),
                ('triple_a', models.IntegerField()),
                ('triple_wa', models.IntegerField()),
                ('floorbed', models.IntegerField()),
                ('cleaning', models.IntegerField()),
                ('security', models.IntegerField()),
                ('extra', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Type',
            fields=[
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_type', models.CharField(choices=[('1', 'Hostel'), ('2', 'House'), ('3', 'Appartment')], max_length=10)),
                ('shareable', models.BooleanField()),
                ('pr_is_personal', models.BooleanField()),
                ('for_business', models.BooleanField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pricing_house',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='pricing_hostel',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='house',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='house',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Pricing_House'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Pricing_Hostel'),
        ),
        migrations.AddField(
            model_name='booking_house',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='booking_house',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='pr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostupload.Property_Upload'),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]