
from django.http import HttpResponse

def maintenance_view(request,exception):
    return HttpResponse("Site under maintenance. Please try again later.", status=503)
