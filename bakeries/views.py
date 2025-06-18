from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. Welcome to our bakery. Ravena")

    return render(request, "index.html")

# Create your views here.
