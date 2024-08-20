from django.db import models

class Device(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='temperature_readings')
    timestamp = models.DateTimeField()
    temperature = models.FloatField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.device.name

class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='humidity_readings')
    timestamp = models.DateTimeField()
    humidity = models.FloatField()

    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return self.device.name
