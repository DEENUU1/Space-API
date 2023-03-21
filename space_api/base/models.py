from django.db import models


class Galaxy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    description = models.TextField()
    age = models.CharField(max_length=120, blank=True, null=True)
    constellation = models.CharField(max_length=120, blank=True, null=True)
    distance = models.CharField(max_length=120, blank=True, null=True)
    type = models.CharField(max_length=120, blank=True, null=True)
    mass = models.CharField(max_length=120, blank=True, null=True)
    number_of_stars = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class System(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    age = models.CharField(max_length=120, blank=True, null=True)
    mass = models.CharField(max_length=120, blank=True, null=True)
    number_of_stars = models.IntegerField(blank=True, null=True)
    star = models.CharField(max_length=120, blank=True, null=True)
    satellites = models.CharField(max_length=120, blank=True, null=True)
    number_of_satellites = models.IntegerField(blank=True, null=True)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE, related_name='systems')

    def __str__(self):
        return self.name


class Planet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    age = models.CharField(max_length=120, blank=True, null=True)
    star = models.CharField(max_length=120, blank=True, null=True)
    number_of_stars = models.IntegerField(blank=True, null=True)
    orbital_period = models.CharField(max_length=120, blank=True, null=True)
    satellites = models.CharField(max_length=120, blank=True, null=True)
    number_of_satellites = models.IntegerField(blank=True, null=True)
    mean_radius = models.CharField(max_length=120, blank=True, null=True)
    mass = models.CharField(max_length=120, blank=True, null=True)
    surface_gravity = models.CharField(max_length=120, blank=True, null=True)
    surface_temp_min = models.CharField(max_length=120, blank=True, null=True)
    surface_temp_max = models.CharField(max_length=120, blank=True, null=True)
    surface_temp_mean = models.CharField(max_length=120, blank=True, null=True)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='planets')

    def __str__(self):
        return self.name
