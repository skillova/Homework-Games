from django.urls import path
from .apps import MainConfig
from .views import index

app_name = MainConfig.name

urlpatterns = [
    path("", index, name="index"),
]
