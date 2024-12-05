
# Create your views here.
from django.shortcuts import render, HttpResponse
from googletrans import Translator  # Import the correct Translator class

# Create your views here.

def home(request):
    if request.method == "POST":
        # Get text and language from the POST request
        text = request.POST.get("translate")
        language = request.POST.get("language")
        
        # Use Google Translator to translate the text
        translator = Translator()
        translation = translator.translate(text, dest=language)
        
        # Return the translated text as an HTTP response
        return HttpResponse(translation.text)
    
    # Render the HTML template for the translation form
    return render(request, "main/index.html")
