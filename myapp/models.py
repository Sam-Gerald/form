from django.db import models

class Visitors(models.Model):
    visitor_id = models.PositiveIntegerField(unique = True) #Unique ID
    name = models.CharField(max_length=50)
    email = models.EmailField()
    category = models.TextField() #This Has Drop Down Box..
    document = models.FileField(upload_to='visitor_documents/', null=True, blank=True)  # Document upload
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.CharField(max_length=200)
    designated_attendee = models.TextField() #This Has Drop Down Box..

    def _str_(self):
        return self.name

