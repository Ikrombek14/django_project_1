from django.urls import path
from .views import first, second, pages

urlpatterns = [
    path('', first),
    path('second/', second),
    path('<str:page>/', pages),
]




