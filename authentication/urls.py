from django.urls import include,path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social'))
]
