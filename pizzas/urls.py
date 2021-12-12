from django.urls import path

from . import views

# app_name helps django distinguish this urls.py file from files
# of the same name in other apps within the project
app_name = "pizzas"


# is a list of individual pages that can be requested from the
# Pizzeria app
urlpatterns = [
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    # the view needs an identifier (pizza_id) so it knows which page to load
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
    path("new_pizza/", views.new_pizza, name="new_pizza"),
    path("new_topping/<int:pizza_id>/", views.new_topping, name="new_topping"),
    path("edit_topping/<int:pizza_id>/", views.edit_topping, name="edit_topping"),
]
