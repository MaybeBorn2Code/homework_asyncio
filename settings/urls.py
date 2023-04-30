# Django
from django.contrib import admin
from django.urls import path

# Local
from main.views import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
]
