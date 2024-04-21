from django.shortcuts import render
from Employe.models import Employes

# Create your views here.
def affichage(request):
    Organisation=Employes.objects.all()
    return render (request, 'employe.html',{'Employes':Employes})