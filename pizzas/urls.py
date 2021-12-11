from django.urls import path

from . import views

# app_name helps django distinguish this urls.py file from files
# of the same name in other apps within the project
app_name = "Pizzeria"


# is a list of individual pages that can be requested from the
# Pizzeria app
urlpatterns = [
    path("", views.index, name="index"),
]
