# middleware.py
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render,redirect
class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            return redirect('maintenance')
        return self.get_response(request)
