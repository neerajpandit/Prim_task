from django.shortcuts import render

# Create your views here.

from .models import Dish

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Dish.objects.filter(name__icontains=query)
    return render(request, 'index.html', {'results': results})
