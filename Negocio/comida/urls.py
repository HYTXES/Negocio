from django.urls import path
from.import views

urlpatterns = [
path('', views.home),
path('bebida/', views.bebida, name='bebida'),



]
