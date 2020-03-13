from django.shortcuts import render
from .models import todo_item
from django.http import  HttpResponseRedirect
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