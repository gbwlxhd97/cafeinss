from django.db import models

class cafeinformation(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=120)
    smoke = models.BooleanField()
    opentime = models.TimeField()
    closetime = models.TimeField()
    atmosphere = models.CharField(max_length=500)
    menu = models.CharField(max_length=500, default="", editable=True)


    def __str__(self):
        return self.name

    def s(self):
        if self.smoke == True:
            return "흡연 가능"
        else:
            return "흡연 불가능"