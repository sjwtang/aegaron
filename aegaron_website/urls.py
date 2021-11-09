from django.urls import path, include
#from . import views

from django.contrib import admin


urlpatterns = [
    path('aegaron/', include('aegaron.urls')),
    path('admin/', admin.site.urls),
]