from django.db import models

# Create your models here.

class Grupe1(models.Model):
    name = models.ForeignKey ("grupe.Grupe",on_delete=models.CASCADE,related_name="grupe",blank=True, null=True)
    adress = models.CharField("Suroga", max_length = 100)
    num_phone = models.IntegerField("Raqami trelfon")
    birth_day = models.DateField("Soli taw")
    nation = models.CharField("Millat", max_length = 100)
    
    
    class Meta:
        verbose_name = 'Груп1'
        verbose_name_plural = 'Групы1'
        
    def __str__(self) -> str:
        return self.adress
