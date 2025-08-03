# grid/models.py
from django.db import models
from django.contrib.auth.models import User

# The Device model represents the physical appliances in the grid,
# such as motors and LEDs.
class Device(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=1)  # Default priority is 1
    status = models.CharField(max_length=50, default='disconnected')

    # This ForeignKey links a device to a specific user.
    # on_delete=models.CASCADE ensures that if a user is deleted,
    # all their devices are also deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# The SensorData model stores the real-time readings from sensors.
# This could be temperature, current, etc.
class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    reading_value = models.FloatField()
    reading_type = models.CharField(max_length=50) # e.g., 'Current', 'Temperature'

    # This links the sensor data to the device it is monitoring.
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.device.name} - {self.reading_type}: {self.reading_value} at {self.timestamp}"

# The Alert model is for notifications about grid anomalies.
class Alert(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_type = models.CharField(max_length=50) # e.g., 'Overloading', 'Power Disconnect'

    # This links the alert to the specific device that caused it.
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alert_type} on {self.device.name} - {self.message}"