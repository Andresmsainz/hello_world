from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World... I'm coming for everything they said I couldn't get!")
