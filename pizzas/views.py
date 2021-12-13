# this is where we process GET and POST requests!

from django.shortcuts import redirect, render
from .forms import PizzaForm, ToppingForm
from .models import Pizza, Topping
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

# when a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file.
def index(request):
    """The home page for pizzas."""
    # the View must point to a Template
    return render(request, "pizzas/index.html")


@login_required
# from urls.py
def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by("date_added")
    # Key is the name of the variable we'll use in the template (HTML)
    ## allows us to access the data
    # Value is the variable used in the view function
    ## this is the data we need to send to the template
    context = {"pizzas": pizzas}
    # pass the context dictionary to the template (HTML) -- allows it to be rendered to the browser
    # the pizzas.html must match the name of our template
    return render(request, "pizzas/pizzas.html", context)


@login_required
# pizza_id used in this views file must match the variable used in urls.py
def pizza(request, pizza_id):
    # just like we did in MyShell.py
    pizza = Pizza.objects.get(id=pizza_id)
    # Make sure the pizza belongs to the current user.
    if pizza.owner != request.user:
        raise Http404
    # FK can be accessed using '_set'
    toppings = pizza.topping_set.all()

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)


@login_required
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
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            form.save()

            return redirect("pizzas:pizzas")
    # display a blank form using the new_pizza.html template
    context = {"form": form}
    return render(request, "pizzas/new_pizza.html", context)


@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            # when we call save(), we include argument (commit=False) to tell Django to create
            # a new topping object & assign it to new_topping w/o saving it to the DB yet
            new_comment = form.save(commit=False)
            # assign the pizza of the new topping based on the pizza we pulled from pizza_id
            new_comment.pizza = pizza
            new_comment.save()
            return redirect("pizzas:pizza", pizza_id=pizza_id)

    context = {"form": form, "pizza": pizza}
    return render(request, "pizzas/new_comment.html", context)


@login_required
def edit_topping(request, topping_id):
    """Edit an existing topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if pizza.owner != request.user:
        raise Http404

    if request.method != "POST":
        # This tells Django to create the form prefilled
        # w info from the existing entry object
        form = ToppingForm(instance=topping)
    else:
        # POST data submitted; process data
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("pizzas:pizza", pizza_id=pizza.id)

    context = {"topping": topping, "pizza": pizza, "form": form}
    return render(request, "pizzas/edit_topping.html", context)
