from django.db import models


class Laptop(models.Model):
    company = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    ram = models.PositiveIntegerField()
    rom = models.PositiveIntegerField()
    price = models.FloatField()
    weight = models.FloatField()
    processor = models.CharField(max_length=35)
    picture = models.ImageField(upload_to='images', default='')
    document = models.FileField(upload_to='files', default='')

    def __str__(self):
        return f"{self.company},{self.model_name},{self.ram},{self.rom},{self.processor},{self.price},{self.weight}"


