import requests
from django.shortcuts import render
from .models import City

# Create your views here.


def weather_index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1442deb6d63d49a6d94e45200a09fea7'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        # Makes the API call and interprets the result in JSON format
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'low_temperature': r['main']['temp_min'],
            'high_temperature': r['main']['temp_max'],
            'humidity': r['main']['humidity'],
            'description': r['weather'][0]['description'],
            'wind': r['wind']['speed'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': city_weather}
    return render(request, 'weather_index.html', context)
