from rest_framework import serializers
from datetime import datetime
'''
Serializer classes process the payloads from the external APIs and generate objects
with just the fields that we need.
'''
class TimestampField(serializers.Field):
    def to_representation(self, value):
        return datetime.fromtimestamp(value).strftime('%Y-%m-%d')
    def to_internal_value(self, value):
        return value

class WeatherDailyItemsSerializer(serializers.Serializer):
    dt = TimestampField(allow_null=False)
    temp = serializers.DictField(required=False, allow_null=True)

class WeatherOnCallSerializer(serializers.Serializer):
    lon = serializers.FloatField(required=True, allow_null=True)
    lat = serializers.FloatField(required=True, allow_null=True)
    daily = serializers.ListSerializer(child=WeatherDailyItemsSerializer(), many=False)

class CitiesSerializer(serializers.Serializer):
    city_name =serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    lat = serializers.FloatField(required=False, allow_null=True)
    long = serializers.FloatField(required=False, allow_null=True)
    result_type = serializers.CharField()

