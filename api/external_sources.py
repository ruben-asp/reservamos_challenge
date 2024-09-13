import requests
from django.conf import settings
from .serializer import CitiesSerializer, WeatherOnCallSerializer

'''
Open Weather API call class
    Constructor:
        - Parameters: lat, lon
    Methods:
        - get_seven_days_forecast()
'''
class WeatherOnCall:
    def __init__(self, lon, lat):
        self.url = settings.OPEN_WEATHER_API_URL + '?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&units=metric&appid={api_key}'.format(
            api_key=settings.OPEN_WEATHER_API_KEY,
            lat=lat,
            lon=lon
        )

    def get_seven_days_forecast(self):
        try:
            response = requests.get(self.url)
            data = response.json()
        except requests.exceptions.RequestException as e:
            return None

        serializer = WeatherOnCallSerializer(data=data, many=False)
        serializer.is_valid(raise_exception=True)

        return serializer.data if serializer.is_valid(raise_exception=True) else {"message": "No data available"}

'''
Open Reservamos API call class
    Constructor:
        - Parameters: city
    Methods:
        - get_cities_coordinates()
        - Return matching cities for the provided city string
'''
class ReservamosAPI:
    def __init__(self, city):
        self.url = settings.RESERVAMOS_API_URL + '?q={city}'.format(city=city)

    def get_cities_coordinates(self):
        try:
            response = requests.get(self.url)
            data = response.json()
        except requests.exceptions.RequestException as e:
            return None

        serializer = CitiesSerializer(data=data, many=True)
        if not serializer.is_valid(raise_exception=True): return None

        return list(filter(lambda d: d['result_type'] == "city", serializer.data))

