from django.shortcuts import render
from my_app.models import Profile
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

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