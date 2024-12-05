from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts),
    path('posts/create/', views.create_post),
    path('CustomUser/', views.get_user),
    path('signUp/',views.create_user),
]
