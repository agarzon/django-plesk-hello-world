from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, world</h1>")
