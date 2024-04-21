
from django.contrib import admin
from django.urls import path
from Employe import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('listes/', views.affichage),
]
