from django.urls import path
from . import views

app_name = "TPG"
urlpatterns = [
    path('', views.index, name="index"), 
    path('generate', views.generate, name='generate'),
    path('results', views.results, name='results')
]