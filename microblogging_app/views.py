from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .supabase_utils import fetch_from_supabase, insert_to_supabase

@api_view(['GET'])
def get_user(request):
    posts = fetch_from_supabase('microblogging_app_customuser')
    return Response(posts)

@api_view(['GET'])
def get_posts(request):
    posts = fetch_from_supabase('posts')
    return Response(posts)

@api_view(['POST'])
def create_post(request):
    data = request.data
    new_post = insert_to_supabase('posts', data)
    return Response(new_post)

