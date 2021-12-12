# this is where we process GET and POST requests!

from django.shortcuts import redirect, render
from .forms import PizzaForm
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
    ## allows us to access the data
    # Value is the variable used in the view function
    ## this is the data we need to send to the template
    context = {"pizzas": pizzas}
    # pass the context dictionary to the template (HTML) -- allows it to be rendered to the browser
    # the pizzas.html must match the name of our template
    return render(request, "pizzas/pizzas.html", context)


# pizza_id used in this views file must match the variable used in urls.py
def pizza(request, pizza_id):
    # just like we did in MySheell.py
    pizza = Pizza.objects.get(id=pizza_id)
    # FK can be accessed using '_set'
    toppings = pizza.topping_set.all()

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)


def new_pizza(request):
    if request.method != "POST":
        # No data submitted; create a blank form (create an instance of PizzaForm)
        # that the user can fill out
        # AKA: if it's a GET request, user will see a blank form
        form = PizzaForm()
    else:
        # POST data submitted; process data
        # if it's a POST request, we load up the data from the form into this variable called form
        # data for the form is pulling from what the user has already posted
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect("pizzas:pizzas")
    # display a blank form using the new_pizza.html template
    context = {"form": form}
    return render(request, "pizzas/new_pizza.html", context)
