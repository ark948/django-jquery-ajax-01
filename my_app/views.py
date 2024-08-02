import json
from django.shortcuts import render, get_object_or_404
from my_app.models import Profile
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.

def index(request):
    return render(request, "index.html")

def with_fetch(request):
    return render(request, "with_fetch.html")


def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles": list(profiles.values())})

# handle ajax made with fetch
def getProfilesV2(request):
    # checks if request is ajax
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        print("request is ajax")
        if request.method == "GET":
            profiles = list(Profile.objects.all().values())
            return JsonResponse({"context": profiles})
        if request.method == "POST":
            data = json.load(request) # deserialize the request object
            profile = data.get('payload')
            Profile.objects.create(name=profile['name'], email=profile['email'])
            return JsonResponse({"status": 'Profile added.'})
        return JsonResponse({'status': 'Invalid Request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        
        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()

        return HttpResponse('New Profile created successfully')
    
def get_profile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    profile = {"id": profile.id, "name": profile.name, "email": profile.email}
    return JsonResponse(profile)
    

def profile(request, profileId):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        profile = get_object_or_404(Profile, id=profileId)
        if request.method == "PUT":
            data = json.load(request)
            updated_value = data.get('payload')

            profile.name = updated_value['name']
            profile.email = updated_value['email']
            profile.save()

            return JsonResponse({'status': 'Profile updated.'})
        if request.method == "DELETE":
            profile.delete()
            return JsonResponse({'status': 'Profile deleted.'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    
def profile_put(request, id):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        profile = get_object_or_404(Profile, id=id)
        if request.method == "PUT":
            data = json.load(request)
            updated_value = data.get('payload')
            profile.name = updated_value['name']
            profile.email = updated_value['email']
            profile.save()
            return JsonResponse({'status': 'Profile updated.'})
        return JsonResponse({'status': 'Invalid requset'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')