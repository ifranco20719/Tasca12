import datetime
from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
    text_pregunta = models.CharField(max_length=200)
    data_publicacio = models.DateTimeField("data publicació")
    
    def __str__(self):
        return self.text_pregunta
    
    def publicat_recentment(self):
        return self.data_publicacio >= timezone.now() - datetime.timedelta(days=1)

class Opcio(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text_opcio = models.CharField(max_length=200)
    vots = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text_opcio
