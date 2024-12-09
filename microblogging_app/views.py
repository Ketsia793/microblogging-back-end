from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .supabase_utils import fetch_from_supabase, insert_to_supabase, delete_from_supabase, getuserby_Id_from_supabase,getuserPost_by_Id_from_supabase
from django.utils import timezone
from datetime import datetime

@api_view(['POST'])
def create_user(request):
    data = request.data
    
    # Hash le mot de passe avant insertion
    if 'password' in data:
        data['password'] = make_password(data['password'])
        
    data['is_staff'] = False
    data['is_active'] = True
    data['is_superuser'] = False
    data['date_joined'] = timezone.now().isoformat()
    print(data)
    new_user = insert_to_supabase('microblogging_app_customuser', data)
    return Response(new_user)

@api_view(['POST'])
def delete_user(request):
    data = request.data
    user = delete_from_supabase('microblogging_app_customuser', data)
    return Response(user)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_userId(request):
    print(f"voici l'id {request.user.id} ")
    # grâce à request.user.id = accès à l'id via le token 
    request.data["id"] = request.user.id 
    data = request.data 
    # pour afficher les infos de l'utilisateur, son id est nécessaire 
    # que l'on obtient grâce à request.user.id qui est contenu dans le token 
    new_post = getuserby_Id_from_supabase('microblogging_app_customuser', data)
    return Response(new_post)

@api_view(['GET'])
def get_user(request):
    users = fetch_from_supabase('microblogging_app_customuser')
    return Response(users)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    request.data["user_id"] = request.user.id
    request.data["created_at"] = datetime.now().date().isoformat()
    data = request.data
    new_post = insert_to_supabase('microblogging_app_post', data)
    return Response(new_post)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_all_posts(request):
    posts = fetch_from_supabase('microblogging_app_post')
    return Response(posts)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_posts(request):
    request.data["user_id"] = request.user.id 
    data = request.data 
    posts = getuserPost_by_Id_from_supabase('microblogging_app_post', data)
    print(posts)
    return Response(posts)






