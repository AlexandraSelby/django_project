from django.http import HttpResponse

def home(request):
    return HttpResponse("Fragrance Club — it works!")
