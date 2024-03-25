from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from api_proj.settings import OPEN_WX_KEY

# Create your views here.


class A_location(APIView):
    def get(self, request, location):
        lat = 32.076176
        lon = -81.088371
        endpoint = f"""https://api.openweathermap.org/data/2.5/weather?lat={
            lat}&lon={lon}&appid={OPEN_WX_KEY}"""
        response = requests.get(endpoint)
        responseJSON = response.json()
        return Response(responseJSON)
