from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_data(request):

    return Response(request.query_params)

@api_view(['POST'])
def post_data(request):

    return Response(dict(body = request.body))