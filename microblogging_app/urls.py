from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('posts/', views.get_posts),
    path('posts/create/', views.create_post),
    path('CustomUser/', views.get_user),
    path('signUp/',views.create_user),
    path('login/', TokenObtainPairView.as_view(), name='login_obtain_pair'),
    path('deleteUser/', views.delete_user),
    path('getUserId/', views.get_userId),
]
