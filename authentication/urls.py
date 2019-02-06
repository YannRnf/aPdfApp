from django.urls import include,path
from . import views

# Auth module router
urlpatterns = [
    # logout route
    path('logout/', views.logout_view, name='logout'),
    # Include the social_django dependency routes, for handling the OAuth2 request and redirect url
    path('', include('social_django.urls', namespace='social'))
]
