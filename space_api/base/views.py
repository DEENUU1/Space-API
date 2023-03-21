from django.shortcuts import render
from .models import Galaxy, Planet, System



def galaxy(request):
    galaktyki = Galaxy.objects.all()
    return render(request, 'galaktyki_wszystkie.html',
                  {'galaktyki': galaktyki})


def systemy(request):
    systemy = System.objects.all()
    return render(request, 'systemy_wszystkie.html',
                  {'systemy': systemy})

def planets(request):
    planety = Planet.objects.all()
    return render(request, 'planety_wszystkie.html',
                  {'planety': planety})

def system_of_galaxy(request):
    galaxy = Galaxy.objects.get(id=2)
    systems = galaxy.systems.all()
    return render(request, 'systemy_dla_galaktyki.html',
                  {'systems': systems})

def planets_of_system(request):
    system = System.objects.get(id=1)
    planets = system.planets.all()
    return render(request, 'planety_z_systemu.html',
                  {'planets': planets})