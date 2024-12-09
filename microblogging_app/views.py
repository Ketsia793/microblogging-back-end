from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .supabase_utils import fetch_from_supabase, insert_to_supabase, delete_from_supabase, getuserby_Id_from_supabase
from django.utils import timezone

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
def get_userId(request):
    data = request.data
    new_post = getuserby_Id_from_supabase('microblogging_app_customuser', data)
    return Response(new_post)

@api_view(['GET'])
def get_user(request):
    users = fetch_from_supabase('microblogging_app_customuser')
    return Response(users)

@api_view(['GET'])
def get_posts(request):
    posts = fetch_from_supabase('posts')
    return Response(posts)

@api_view(['POST'])
def create_post(request):
    data = request.data
    new_post = insert_to_supabase('posts', data)
    return Response(new_post)







