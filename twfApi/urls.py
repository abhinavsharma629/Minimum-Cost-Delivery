from django.urls import include, path
from . import views

urlpatterns = [
    path('getMinimumCost', views.getMinimumCost, name='getMinimumCost'),
]