from django.db import models
from django.contrib.auth.models import User

Instruments = ["Guitare", "Piano"]


class Request(models.Model):
    requestTitle = models.CharField(max_length=50)
    requestCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    requestInstrument = models.CharField(max_length=50, blank=True)
    requestDescription = models.TextField(max_length=500)

    def __str__(self):
        return "%s " % (self.RequestTitle)

    class Meta:
        db_table = "request"
