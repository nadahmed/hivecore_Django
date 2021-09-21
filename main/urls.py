from . import views
from django.urls import path , include

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
]