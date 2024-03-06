from django.db import models

# Create your models here.

class Grupe(models.Model):
    name = models.CharField("Name",max_length = 100, blank = True, null = True)
    adress = models.CharField("Suroga", max_length = 100)
    num_phone = models.IntegerField("Raqami trelfon")
    birth_day = models.DateField("Soli taw")
    nation = models.CharField("Millat", max_length = 100)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Груп'
        verbose_name_plural = 'Групы'
        
        def __str__(self) -> str:
            return self.name
