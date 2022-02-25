from django.contrib import admin 
from django.urls import path 
from api import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ceps/', views.CepAPI.as_view()),
    path('ceps/<str:pk>/', views.CepAPI.as_view())
]
