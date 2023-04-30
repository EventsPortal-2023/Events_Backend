from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# a model to store the data for the events 
class Events(models.Model):
    eventDescription = models.TextField()
    eventSummary = models.CharField(max_length=500)
    eventtitle= models.CharField(max_length=100)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventSeatingCapacity = models.IntegerField()
    eventVenue = models.TextField()
    registrationLink = models.URLField()
    is_referral = models.BooleanField(default=False)
    contactName1 = models.CharField(max_length=100, default="dummy user")
    contactName2 = models.CharField(max_length=100, blank=True, null=True)
    contactNumber1 = models.CharField(max_length=10, default="0000000000")
    contactNumber2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return str(self.eventtitle) + " " + str(self.eventDate.year)


# model for the gallery in events
class Photo(models.Model):  
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.event.title + "_" + self.desc



# a model to store the likes by users
class EventLikes(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "EventLikes"
        verbose_name_plural = "EventLikes"