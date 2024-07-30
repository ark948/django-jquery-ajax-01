from django.shortcuts import render
from my_app.models import Profile

# Create your views here.

def index(request):
    return render(request, "index.html")