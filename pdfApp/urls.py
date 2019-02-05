from django.contrib import admin
from django.urls import include,path
from authentication import views as defaultViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('auth/', include('authentication.urls')),
    path('', defaultViews.index),
]
