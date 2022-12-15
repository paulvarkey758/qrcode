from django.db import models

# Create your models here.
class Mymodel(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=20,unique=True)
    qrCode=models.ImageField(upload_to="img/")

    def __str__(self):
        return self.name