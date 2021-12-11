from django.shortcuts import render

# Create your views here.

# when a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file.


def index(request):
    """The home page for Pizzeria."""
    # the View must point to a Template
    return render(request, "Pizzeria/index.html")
