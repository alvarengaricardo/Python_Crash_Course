from django.shortcuts import render

# Create your views here.

def index(request):
    """Página inicial"""
    return render(request, 'learning_logs/index.html')