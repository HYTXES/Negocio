from django.urls import path
from.import views

urlpatterns = [
path('', views.bebida),
path('bebida/', views.bebida, name='bebida'),

]
