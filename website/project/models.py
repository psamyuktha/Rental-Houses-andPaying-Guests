from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.



class Amenities(models.Model):
    am_id = models.IntegerField(primary_key=True)
    amenities = models.CharField(max_length=100)

    def __str__(self):
        return self.amenities


class Property_Type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()


class Property_Upload(models.Model):
    pr_id = models.IntegerField(primary_key=True)
    pr_type = models.OneToOneField(Property_Type, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    shareable = models.BooleanField()
    pr_is_personal = models.BooleanField()
    for_business = models.BooleanField()


class Pricing_House(models.Model):
    pr_id = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    floorbed = models.IntegerField()
    cleaning = models.IntegerField()
    security = models.IntegerField()
    extra = models.IntegerField()

class House(models.Model):
    pr_id = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    floorbed = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    price = models.OneToOneField(Pricing_House , on_delete=models.CASCADE)
    avg_rating = models.IntegerField()
    description = models.TextField()
    gallery = models.URLField()
    guest = models.IntegerField()


class Pricing_Hostel(models.Model):
    pr_id = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    four_a = models.IntegerField()
    four_wa = models.IntegerField()
    cleaning = models.IntegerField()
    security = models.IntegerField()
    cab = models.IntegerField()
    food = models.IntegerField()
    extra = models.IntegerField()



class Hostel(models.Model):
    pr_id = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    four_a = models.IntegerField()
    four_wa = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    price = models.OneToOneField(Pricing_Hostel , on_delete=models.CASCADE)
    avg_rating = models.IntegerField()
    description = models.TextField()
    gallery = models.URLField()



class Booking_House(models.Model):
    booking_id = models.AutoField(primary_key=True)
    Pr_id = models.OneToOneField(Property_Upload,on_delete=models.CASCADE)
    user_id = models.OneToOneField(User , on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    single_a = models.IntegerField(null=True)
    single_wa = models.IntegerField(null=True)
    double_a = models.IntegerField(null=True)
    double_wa = models.IntegerField(null=True)
    triple_a = models.IntegerField(null=True)
    triple_wa = models.IntegerField(null=True)
    floorbed = models.IntegerField(null=True)
    price_paid = models.IntegerField()
    Rating = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    Feedback = models.TextField(null=True)



class Booking_Hostel(models.Model):
    pr_id = models.OneToOneField(Property_Upload,on_delete=models.CASCADE)
    user_id = models.OneToOneField(User , on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    single_a = models.IntegerField(null=True)
    single_wa = models.IntegerField(null=True)
    double_a = models.IntegerField(null=True)
    double_wa = models.IntegerField(null=True)
    triple_a = models.IntegerField(null=True)
    triple_wa = models.IntegerField(null=True)
    price_paid = models.IntegerField()
    Rating = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    Feedback = models.TextField(null=True)


class detail(models.Model):
    place = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()