from django.shortcuts import render


# Create your views here.

def todo_view(request):
    return render(request, "home/home.html",{})