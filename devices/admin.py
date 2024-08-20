from django.contrib import admin
from .models import HumidityReading,TemperatureReading,Device
# Register your models here.


admin.site.register(HumidityReading)
admin.site.register(TemperatureReading)
admin.site.register(Device)