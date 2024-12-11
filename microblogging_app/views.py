from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Profil, Post 
from .supabase_utils import fetch_from_supabase, insert_to_supabase, new_insert_to_supabase, delete_from_supabase, getuserby_Id_from_supabase,getuserPost_by_Id_from_supabase,updateuser_profil_by_Id_from_supabase
from django.utils import timezone
from datetime import datetime

# @api_view(['POST'])
# def create_user(request):
#     data = request.data
    
#     # Hash le mot de passe avant insertion
#     if 'password' in data:
#         data['password'] = make_password(data['password'])
        
#     data['is_staff'] = False
#     data['is_active'] = True
#     data['is_superuser'] = False
#     data['date_joined'] = timezone.now().isoformat()
#     print(data)
#     new_user = insert_to_supabase('microblogging_app_customuser', data)
    
#     if new_user and 'id' in new_user:
#         profil_data = {
#             'user': new_user['id'],
#             'username':new_user['username'],
#             'bio' : '',
#             'image':'default.jpg',
#             'created_at':timezone.now().date().isoformat(),
#             'update_at':None
#         }
#     new_profil = insert_to_supabase('microblogging_app_profil', profil_data)
#     return Response({'user':new_user, 'profile':new_profil})

@api_view(['POST'])
def create_user(request):
    data = request.data
    
    # Hash le mot de passe avant insertion
    if 'password' in data:
        data['password'] = make_password(data['password'])
        
    # la condition de la création du username c'est l'email
    base_username = data['email'].split('@')[0]
    username = base_username
    counter = 1
    
    # la boucle conditionne l'existence du username pour éviter toute répétition
    while CustomUser.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1
        
    print(data)
    user = CustomUser.objects.create(
        username =username,
        last_name =data['last_name'],
        first_name =data['first_name'],
        email=data['email'],
        password=data['password'],
        is_staff =False,
        is_active =True,
        is_superuser =False,
        date_joined =timezone.now().isoformat()
    )
    
    
    profil_data = {
        'user_id': user.id,  # Use .id instead of ['id']
        'username': user.username,  # Use .username instead of ['username']
        'bio': '',
        'image': 'default.jpg',
        'created_at': timezone.now().date().isoformat(),
        'update_at': None
    }
    new_profil = new_insert_to_supabase('microblogging_app_profil', profil_data)
    return Response({'user': user.id, 'profile': new_profil})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_profil(request):
    request.data["user_id"] = request.user.id 
    data = request.data 
    profil = getuserPost_by_Id_from_supabase('microblogging_app_profil', data)
    print(profil)
    return Response(profil)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def put_user_profil(request):
    request.data["user_id"] = request.user.id
    data = request.data 
    profil = getuserPost_by_Id_from_supabase('microblogging_app_profil', data)
    request.data["profil_id"] = profil['details'][0]['profil_id']
    request.data["image"] = profil['details'][0]['image']
    request.data["created_at"] = profil['details'][0]['created_at']
    request.data["username"] = profil['details'][0]['username']
    data = request.data 
    profil = updateuser_profil_by_Id_from_supabase('microblogging_app_profil', data)
    print(f"Ceci est le profil{profil}")
    return Response(profil)


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






