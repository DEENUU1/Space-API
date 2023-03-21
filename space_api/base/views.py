from django.shortcuts import render
from models import Galaxy, Planet, System



system = System.objects.get(name="Solar System")
planets = system.planets.all()

