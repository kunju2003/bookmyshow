from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def movie(request):
    return render(request,'movie.html')