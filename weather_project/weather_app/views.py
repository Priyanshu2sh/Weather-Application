from django.shortcuts import render, get_object_or_404
import requests
from .models import City

# Define constants
API_KEY = '478ff723f84c562cd02e799dc840d4e9'
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


def index(request):
    # Retrieve all cities from the database
    cities = City.objects.all()

    # Handle POST request
    if request.method == 'POST':
        city = request.POST['city']
        city = city.lower()

        # Check if the city already exists in the database
        city_exists = City.objects.filter(name=city)
        if not city_exists:
            
            # Fetch weather data for the new city
            weather_data = fetch_weather(city, API_KEY, current_weather_url)

            # Check if the weather data was successfully fetched
            if weather_data['status'] == 200:
                context = {
                    'weather_data': weather_data,
                    'cities': cities,
                }

                # Save the new city to the database
                new_city=City(name=city)
                new_city.save()
                return render(request, 'weather_app/index.html', context)
            else:
                context = {
                    'error': 'City not found, Make sure that the spelling of the city is correct!',
                    'cities': cities,
                }
                return render(request, 'weather_app/index.html', context)

        else:
            # Fetch weather data for the existing city
            weather_data = fetch_weather(city, API_KEY, current_weather_url)

            context = {
                'weather_data': weather_data,
                'cities': cities,
            }
            return render(request, 'weather_app/index.html', context)
    else:
        # Handle GET request
        context = {
            'cities': cities,
        }
        return render(request, 'weather_app/index.html', context)
    
def fetch_weather(city, api_key, current_weather_url):
    # Fetch weather data from the OpenWeatherMap API
    response = requests.get(current_weather_url.format(city, api_key)).json()

    # Check if the API request was successful
    if response['cod'] != 200:
        weather_data = {
           'status': response['cod'],
        }
        return weather_data
    else:
        weather_data = {
            'city': city,
            'status': response['cod'],
            'temperature': round(response['main']['temp'] - 273.15, 2),
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        return weather_data
    
def retrieve_city_weather(request, cityname):
    # Retrieve all cities from the database
    cities = City.objects.all()
    
    # Check if a city name was provided
    if cityname:
        # Fetch weather data for the specified city
        weather_data = fetch_weather(cityname, API_KEY, current_weather_url)

        # Check if the weather data was successfully fetched
        if weather_data['status'] == 200:
            context = {
                'weather_data': weather_data,
                'cities': cities,
            }
            return render(request, 'weather_app/index.html', context)
        else:
            context = {
                'error': 'City not found, Make sure that the spelling of the city is correct!',
                'cities': cities,
            }
            return render(request, 'weather_app/index.html', context)
    else:
        context = {
            'error': 'City not found, Make sure that the spelling of the city is correct!',
            'cities': cities,
        }
        return render(request, 'weather_app/index.html', context)

def delete_city_api(request, cityname):
    try:
        # Retrieve the city object from the database
        city = get_object_or_404(City, name=cityname)

        # Delete the city from the database
        city.delete()

        # Retrieve all cities from the database
        cities = City.objects.all()

        # Render the index template with a success message
        return render(request, 'weather_app/index.html', {'cities': cities, 'message': f'{cityname} has been deleted.'})
    except Exception as e:
        # Render the index template with an error message
        return render(request, 'weather_app/index.html', {'error': f'Error deleting {cityname}: {e}'})