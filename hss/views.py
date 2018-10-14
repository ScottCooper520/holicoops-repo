from django.shortcuts import render

# Create your views here.
def holiday_ss(request):
    return render(request, 'hss/holiday_ss.html', {})
