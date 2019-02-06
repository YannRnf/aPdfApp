from django.contrib import admin
from django.urls import include,path
from authentication import views as defaultViews

# Global Router
urlpatterns = [
    # Native Django admin routes
    path('admin/', admin.site.urls),
    # Home routes for a connected user
    path('home/', include('home.urls')),
    # Auth routes for handling oauth, logout and user connection page
    path('auth/', include('authentication.urls')),
    # Default route pointing to auth module "index" route
    path('', defaultViews.index),
]
