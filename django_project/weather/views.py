from django.shortcuts import render, get_object_or_404, redirect
import requests

from .forms import CityForm
from .models import City
# Create your views here.
def main(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=kr&appid=d9459d4d358dc8f356be115742c06405'
    cities = City.objects.all()

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    weather_data = []
    for city in cities:
        try:
            city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
            print(city_weather)
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }

            weather_data.append(weather)  # add the data for the current city into our list
        except KeyError:
            city = get_object_or_404(City, name=city.name)
            city.delete()
            error_message = "존재하지 않는 도시입니다!"
            return render(request, 'weather/error.html', {'error_message': error_message})

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/main.html', context)

def delete_city(request, city_id):
    task = get_object_or_404(City, name=city_id)
    task.delete()
    return redirect('weather:main')