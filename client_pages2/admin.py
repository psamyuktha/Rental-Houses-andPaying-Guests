from django.contrib import admin
from .models import Amenities,Property_Type, Address,detail,Property_Upload,Pricing_House,House,Pricing_Hostel,Hostel,Booking_House,Bed_Type,Booking_Hostel

# Register your models h
admin.site.register(Amenities)
admin.site.register(Property_Type)
admin.site.register( Address)
admin.site.register(Property_Upload)
admin.site.register(Pricing_House)
admin.site.register(House)
admin.site.register(Pricing_Hostel)
admin.site.register(Hostel)
admin.site.register(Booking_House)
admin.site.register(Bed_Type)
admin.site.register(Booking_Hostel)
admin.site.register(detail)
