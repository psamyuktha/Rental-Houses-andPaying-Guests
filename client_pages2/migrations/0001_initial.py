# Generated by Django 2.1.3 on 2018-12-01 20:26

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
                ('am_id', models.IntegerField(primary_key=True, serialize=False)),
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
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('price_paid', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('status', models.IntegerField()),
                ('Feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking_House',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
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
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('guests', models.IntegerField()),
                ('singlerooms', models.CharField(choices=[('0', 'ZERO'), ('1', 'ONE'), ('2', 'TW0'), ('3', 'THREE')], default='1', max_length=6)),
                ('singlerooms_attached', models.CharField(choices=[('0', 'ZERO'), ('1', 'ONE'), ('2', 'TW0'), ('3', 'THREE')], default='1', max_length=6)),
                ('doublerooms', models.CharField(choices=[('0', 'ZERO'), ('1', 'ONE'), ('2', 'TW0'), ('3', 'THREE')], default='1', max_length=6)),
                ('doublerooms_attached', models.CharField(choices=[('0', 'ZERO'), ('1', 'ONE'), ('2', 'TW0'), ('3', 'THREE')], default='1', max_length=6)),
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
                ('avg_rating', models.IntegerField()),
                ('description', models.TextField()),
                ('gallery', models.CharField(max_length=5000)),
                ('amenities', models.ManyToManyField(to='client_pages2.Amenities')),
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
                ('gallery1', models.URLField(null=True)),
                ('gallery2', models.URLField(null=True)),
                ('guest', models.IntegerField()),
                ('amenities', models.ManyToManyField(to='client_pages2.Amenities')),
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
                ('pr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pr_type', models.IntegerField()),
                ('shareable', models.BooleanField()),
                ('pr_is_personal', models.BooleanField()),
                ('for_business', models.BooleanField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Address')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pricing_house',
            name='pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='pricing_hostel',
            name='pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='house',
            name='pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='house',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Pricing_House'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='price',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Pricing_Hostel'),
        ),
        migrations.AddField(
            model_name='booking_house',
            name='Pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='booking_house',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='Pr_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Property_Upload'),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='bed_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client_pages2.Bed_Type'),
        ),
        migrations.AddField(
            model_name='booking_hostel',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
