import requests
from django.shortcuts import render
from .models import City
import os

# Create your views here.


def weather_index(request):
    API_KEY = os.environ.get('WEATHER_API')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + API_KEY

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        # Makes the API call and interprets the result in JSON format
        response = requests.get(url.format(city))
        r = response.json()
        city_weather = {
            'city': city.name,
            'low_temperature': r['main']['temp_min'],
            'high_temperature': r['main']['temp_max'],
            'humidity': r['main']['humidity'],
            'description': r['weather'][0]['description'],
            'wind': r['wind']['speed'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data}
    return render(request, 'weather_index.html', context)
