from django.db import models


class Galaxy(models.Model):
    name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    constellation = models.CharField(max_length=120)
    distance = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    mass = models.CharField(max_length=120)
    number_of_stars = models.CharField(max_length=120)
    size = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    mass = models.CharField(max_length=120)
    star = models.CharField(max_length=120)
    satellites = models.CharField(max_length=120)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE, related_name='systems')

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    star = models.CharField(max_length=120)
    orbital_period = models.CharField(max_length=120)
    satellites = models.CharField(max_length=120)
    mean_radius = models.CharField(max_length=120)
    mass = models.CharField(max_length=120)
    surface_gravity = models.CharField(max_length=120)
    surface_temp_min = models.CharField(max_length=120)
    surface_temp_max = models.CharField(max_length=120)
    surface_temp_mean = models.CharField(max_length=120)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='planets')

    def __str__(self):
        return self.name