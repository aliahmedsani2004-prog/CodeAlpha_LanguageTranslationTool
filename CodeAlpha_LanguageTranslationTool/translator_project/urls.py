from django.contrib import admin
from django.urls import path
from translate_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.translate_view, name='translate'),
]