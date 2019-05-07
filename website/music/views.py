from django.http import HTTPResponse

# Create your views here.
def index (request):
    return HTTPRespond("<h1>This is the Music Hompage")