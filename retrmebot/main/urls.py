from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('load_to_db', views.load_to_db, name='load_to_db'),
    path('get_from_db', views.get_from_db, name='get_from_db'),
]
