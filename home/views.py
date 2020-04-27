from django.shortcuts import render
from .models import todo_item
from django.http import  HttpResponseRedirect
from .serializers import todoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Create your views here.

def todo_view(request):
    all_todo_item=todo_item.objects.all()
    return render(request, "home.html",
    {'all_items': all_todo_item})


def add_todo(request):
    c=request.POST['content']
    new_item=todo_item(content=c)
    new_item.save()
    return HttpResponseRedirect('/')


def del_todo(request, todo_id):
    item_delete=todo_item.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/')

class todo_api(viewsets.ModelViewSet):
    serializer_class=todoSerializer
    queryset=todo_item.objects.all()