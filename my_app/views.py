from django.shortcuts import render
from my_app.models import Profile
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "index.html")


def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles": list(profiles.values())})