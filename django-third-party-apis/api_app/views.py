from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from api_proj.settings import GNEWS_API_KEY

# Create your views here.


class A_article(APIView):

    def get(self, request, name):
        endpoint = f"""https://gnews.io/api/v4/search?q={
            name}&max=1&apikey={GNEWS_API_KEY}"""
        response = requests.get(endpoint)
        responseJSON = response.json()
        client_response = {
            'title': responseJSON['articles'][0]['title'],
            'description': responseJSON['articles'][0]['description'],
            'url': responseJSON['articles'][0]['url']
        }
        return Response(client_response)
