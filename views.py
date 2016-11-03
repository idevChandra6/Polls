from django.http import HttpResponse


def index(request):
    return HttpResponse("iOS Vending App User-Interface goes on this page.")
