

from django.http import HttpResponse
from PIL import Image

#def image_load(request):
 #   print("\nImage Loaded\n")
 #   red = Image.new('RGB', (1, 1))
 #   response = HttpResponse(content_type="image/png")
 #   red.save(response, "PNG")
 #   return response

def homePageView(request):
    return HttpResponse("Hello, World!")