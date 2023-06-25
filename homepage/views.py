from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile, URLs

def profile(request):
    # Assuming you have a unique identifier for your profile, such as an ID or a slug
    profile_id = 1  # Replace with the actual ID or slug of your profile

    # Retrieve the profile from the database
    profile = get_object_or_404(Profile, id=profile_id)  # Assuming 'id' is the field used for the unique identifier
    print(profile.name, profile.bio)

    context = {'profile': profile}
   
    return render(request, 'homepage.html', context)