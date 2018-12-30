from django.shortcuts import render
from .models import Slide
from django.http import HttpResponse

# Create your views here.
def holiday_ss(request):
    # images = Slide.image
    # caption = Slide.title + " " + Slide.description
    # return render(request, 'hss/holiday_ss.html', {'caption': caption})
    # return render(request, 'hss/holiday_ss.html', {'images': images, "captions": captions})
    slides = Slide.objects.all()
    return render(request, 'hss/holiday_ss.html', {'slides': slides})

# ok http://127.0.0.1:8000/hello
def hello(request):
    return HttpResponse("Hello response...")

# ok http://127.0.0.1:8000/api
def api(request):
    return HttpResponse("Hello API...")