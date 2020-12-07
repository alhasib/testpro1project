from django.shortcuts import render
from .models import *
# Create your views here.
def profile(request):
    p = Profile.objects.all()
    context = {'profile':p}
    return render(request, 'profile.html', context)