from django.shortcuts import render

# Create your views here.


def weather_index(request):
    return render(request, 'weather_index.html')
