from django.shortcuts import render

# Create your views here.
def bookcove(request):
    return render(request, "designapp/bookcover.html")