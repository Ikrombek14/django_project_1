from .views import get_name, get_age
from django.urls import path

urlpatterns = [
    path("1", get_name, name="name"),
    path("2", get_age, name="age")

]