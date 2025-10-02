from django.shortcuts import render

def index(request):
    context = {
        'page_number': 'index',
    }
    return render(request, 'main/index.html', context)
