from django.shortcuts import render;
from django.http import JsonResponse
from django.middleware.csrf import get_token

# class Report:
#     def home_page(request):
#         context = {
#             'page title': 'home page',
#         }
#         return JsonResponse(context)

def get_csrf_token(request):
    csrf_token = get_token(request)

    return JsonResponse({"csrf_token": csrf_token})