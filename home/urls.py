from django.urls import path
from . import views

# Home module router
urlpatterns = [
    # Home page route
    path('', views.index, name='index'),
]
