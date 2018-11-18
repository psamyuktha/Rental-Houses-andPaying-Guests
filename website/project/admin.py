from django.contrib import admin


from .models import Amenities
from .models import Property_Upload
from .models import Address
from .models import Pricing_Hostel
from .models import Pricing_House
from .models import Property_Type
from .models import Hostel
from .models import House
from .models import Booking_Hostel
from .models import Booking_House
from .models import detail


# Register your models here.


admin.site.register(Address)
admin.site.register(Amenities)
admin.site.register(Booking_House)
admin.site.register(Booking_Hostel)
admin.site.register(House)
admin.site.register(Hostel)
admin.site.register(Property_Type)
admin.site.register(Pricing_Hostel)
admin.site.register(Property_Upload)
admin.site.register(Pricing_House)
admin.site.register(detail)


