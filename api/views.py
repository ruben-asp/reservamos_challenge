from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
logger = logging.getLogger(__name__)

from .external_sources import WeatherOnCall, ReservamosAPI

# Create your views here.
@api_view(['GET'])
def get_data(request, city= None):
    # If no parameter provided, return some usage instructions
    if city is None:
        logger.info("No city provided, exit...")
        return Response({"Usage": "api_url/<city>"})

    logger.info("Getting '{}' matching cities...".format(city))

    # Gett all matching cities from Reservamos API
    __reservamos_obj = ReservamosAPI(city)
    __cities = __reservamos_obj.get_cities_coordinates()

    # Exit if any
    if __cities is None: return Response({"message": "No data available"})

    # Get the 7 days forecast for each city and include it on the payload
    for __city in __cities:
        logger.info("--> Getting forecast for city: {city_name}".format(**__city))
        __weather_obj = WeatherOnCall(lat=__city['lat'], lon=__city['long'])
        __seven_days_forecast = __weather_obj.get_seven_days_forecast()
        __city['seven_days_forecast'] = __seven_days_forecast.get('daily', [])[:7]

    # Return a JSON payload
    return Response(__cities)

