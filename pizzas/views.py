from django.shortcuts import render

from .models import Pizza

# Create your views here.

# when a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file.


def index(request):
    """The home page for pizzas."""
    # the View must point to a Template
    return render(request, "pizzas/index.html")


# from urls.py
def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")

    # Key is the name of the variable we'll use in the template (HTML)
    # Value is the variable used in the view function
    context = {"pizzas": pizzas}

    # pass the context dictionary to the template (HTML) -- allows it to be rendered to the browser
    return render(request, "pizzas/pizzas.html", context)
