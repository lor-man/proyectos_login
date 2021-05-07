from django.db import models

# Create your models here.

class paciente(models.Model):
    nombre= models.CharField(max_length=30)
    edad= models.PositiveSmallIntegerField()
    peso= models.FloatField()
    altura=models.FloatField()
    fecha=models.DateField()
    hora=models.TimeField()
    created =models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)