from django.db import models


# Create your models here.
from django.contrib.auth.models import User


TYPE_CHOICES=(
    ('1', 'Hostel'),
    ('2','House'),
    ('3','Appartment')
    )


class Amenities(models.Model):
    am_id = models.AutoField(primary_key=True)
    amenities = models.CharField(max_length=100)
    def __str__(self):
        return self.amenities

class refrence_Amenities(models.Model):
    am_id = models.AutoField(primary_key=True)
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
    pr_type = models.CharField(choices=TYPE_CHOICES,max_length=10)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shareable = models.BooleanField()
    pr_is_personal = models.BooleanField()
    for_business = models.BooleanField()

class Pricing_House(models.Model):
    pr = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
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
    pr = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    floorbed = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    price = models.OneToOneField(Pricing_House , on_delete=models.CASCADE)
    avg_rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
    gallery = models.URLField(null=True)
    guest = models.IntegerField(null=True)

class Pricing_Hostel(models.Model):
    pr = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
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
    pr = models.OneToOneField(Property_Upload , on_delete=models.CASCADE)
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
    avg_rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
    gallery = models.URLField(null=True)



class Booking_House(models.Model):
    pr = models.OneToOneField(Property_Upload,on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    single_a = models.IntegerField()
    single_wa = models.IntegerField()
    double_a = models.IntegerField()
    double_wa = models.IntegerField()
    triple_a = models.IntegerField()
    triple_wa = models.IntegerField()
    floorbed = models.IntegerField()
    price_paid = models.IntegerField()
    Rating = models.IntegerField()
    status = models.IntegerField()
    Feedback = models.TextField()

class Bed_Type(models.Model):
    b_id = models.AutoField(primary_key=True)
    bed_name = models.CharField(max_length=50)


class Booking_Hostel(models.Model):
    pr = models.OneToOneField(Property_Upload,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    single_a = models.IntegerField(null=True)
    single_wa = models.IntegerField(null=True)
    double_a = models.IntegerField(null=True)
    double_wa = models.IntegerField(null=True)
    triple_a = models.IntegerField(null=True)
    triple_wa = models.IntegerField(null=True)
    four_a = models.IntegerField(null=True)
    four_wa = models.IntegerField(null=True)
    price_paid = models.IntegerField()
    Rating = models.IntegerField()
    status = models.IntegerField()
    Feedback = models.TextField()
