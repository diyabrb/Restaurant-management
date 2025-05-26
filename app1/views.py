from django.shortcuts import render
from .models import Menu,contact
from .forms import contactform

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def menu(request):
    d2 ={
        'menu':Menu.objects.all()
    }
    return render(request,"menu.html",d2)
def contact(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            form = contactform()  # reinitialize after saving
    else:
        form = contactform()  # initialize blank form for GET

    d3 = {
        'form': form
    }
    return render(request, "contact.html", d3)
