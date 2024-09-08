from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

from .forms import Form
# Create your views here.

def cont(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/contact/")
    else:
        form = Form()
    
    


    return render(request, 'contact/cont.html', {"form": form})