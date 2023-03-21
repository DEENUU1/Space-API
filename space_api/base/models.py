from django.db import models


class Galaxy(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=120)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE, related_name='systems')
    
    def __str__(self):
        return self.name