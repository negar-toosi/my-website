from django.http import HttpResponse
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if maintenance mode is enabled
        if settings.MAINTENANCE_MODE:
            # Serve maintenance page
            return HttpResponse("This site is currently under maintenance. Please try again later.", status=503)

        # Continue processing other middleware and view
        response = self.get_response(request)
        return response
