from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .chatgptfunction import generate_image_from_prompt
import base64

# Create your views here.
def index(request):
    return render(request, 'index.html' )

def generate_image(request):
    if request.method == 'POST':
        # Get the text input from the user
        prompt = request.POST.get('prompt')

        # Use the DALL-E API to generate an image from the text
        image_data = generate_image_from_prompt(prompt)
        print(image_data)
        image_url = image_data[0].get("url")

        # Return the image to the user
        return render(request, 'generate_image.html', {"image_url":image_url})

    # If the request is not a POST request, return the form to the user
    return render(request, 'generate_image.html')

