from django.shortcuts import render
from .models import Game

def index(request):
    games_data = Game.objects.all().order_by('article')
    context = {
        'page_number': 'index',
        'games': games_data
    }
    return render(request, 'main/index.html', context)
