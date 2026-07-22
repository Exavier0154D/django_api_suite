from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    response = requests.get(settings.API_URL)  # Solicitud a la API
    posts = response.json()  # Convertir respuesta a JSON

    total_responses = len(posts) # Número total de respuestas

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }

    return render(request, 'dashboard/index.html', data)