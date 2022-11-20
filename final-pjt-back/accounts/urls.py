from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('profile/post/<str:username>/', views.user_post),
]