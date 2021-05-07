from django.db import models

# Create your models here.
class boletoAerolinea(models.Model):
    nombre= models.CharField(max_length=30)
    vuelo= models.PositiveSmallIntegerField()
    srcClss1=models.PositiveSmallIntegerField()
    srcClss2=models.PositiveSmallIntegerField()
    srcClss3=models.PositiveSmallIntegerField()
    subTotal= models.FloatField()
    descuento=models.FloatField()
    total=models.FloatField()
    created =models.DateTimeField(auto_now_add=True)
    