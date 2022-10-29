from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse 


def info(request):
      return JsonResponse({"slackUsername" : "labanrotich", "backend" : True, "age" : 25, "bio" : " i am a software developer from kenya"}) 
