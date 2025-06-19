from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Bakery


def index(request):
    context = {
        "bakeries": Bakery.objects.all()
    }
    return render(request, "index.html", context)

def indexcopy(request, pk):
    bakery = get_object_or_404(Bakery, pk=pk)

    return render(request, 'indexcopy.html', {
        'bakery': bakery
    })