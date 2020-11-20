from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "users/home.html")
