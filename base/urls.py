from django.contrib import admin
from django.urls import path
from . import views
from .views import register_student
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    # path('', views.index),  
    path('students/<int:id>',views.MyStudentsView.as_view()),
    path('students/',views.MyStudentsView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register),
    path('register_student/', views.register_student, name='register_student'),

]
