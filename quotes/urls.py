
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('addStock.html', views.addStock, name='addStock'),
    path('delete/<stockId>', views.delete, name="delete"),
    path('addStock.html', views.addStock, name='addStock'),
    path('deleteStock.html', views.deleteStock, name='deleteStock'),
    path('delete1/<stockId>', views.delete1, name="delete1"),



]