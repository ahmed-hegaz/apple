from django.urls import path
from .import views

app_name = 'apple'

urlpatterns = [
     path('', views.apple_list, name = 'apple_list'),
     path('<int:id>', views.apple_detail, name = 'apple_detail'),
    
]
