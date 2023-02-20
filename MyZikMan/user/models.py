from django.db import models

class Band(models.Model):
    bandName = models.CharField(max_length=50)
    bandEmail = models.EmailField()
    bandStyle = models.CharField(max_length=50)

    def __str__(self):
        return "%s " %(self.bandName)

    class Meta:
        db_table = "band"

class User(models.Model):
    userName = models.CharField(max_length=50)
    userEmail = models.EmailField()
    userInstrument = models.CharField(max_length=50)
    userBand = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return "%s " %(self.userName)

    class Meta:
        db_table = "user"
