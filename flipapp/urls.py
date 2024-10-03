from django.urls import path 
from.import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
]
