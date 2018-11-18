from django.contrib import admin
from .models import variables,Amenities,Property_Type,Address,Property_Upload,Pricing_House,House,Pricing_Hostel,Hostel,Booking_House,Booking_Hostel
admin.site.register(variables)
# Register your models here.
admin.site.register(Amenities)
admin.site.register(Property_Type)
admin.site.register(Address)
admin.site.register(Property_Upload)
admin.site.register(Pricing_House)
admin.site.register(House)
admin.site.register(Pricing_Hostel)
admin.site.register(Hostel)
admin.site.register(Booking_House)
admin.site.register(Booking_Hostel)
