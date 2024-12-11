from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('posts/', views.get_all_posts),
    path('posts/create/', views.create_post),
    path('CustomUser/', views.get_user),
    path('signUp/',views.create_user),
    path('login/', TokenObtainPairView.as_view(), name='login_obtain_pair'),
    path('deleteUser/', views.delete_user),
    path('getUserId/', views.get_userId),
    path('getUserpost/', views.get_user_posts),
    path('getUserProfil/',views.get_user_profil),
    path('putUserProfil/', views.put_user_profil),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
