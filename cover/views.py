from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'cover/home.html')

def index2(request):
	return render(request, 'cover/mission.html')

def index3(request):
    return render(request, 'cover/donations.html')