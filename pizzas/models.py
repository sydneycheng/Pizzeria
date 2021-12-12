from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    # auto_now_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)

    # Allows the "name" of the Pizza to be displayed
    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # allows us to set a special attribute telling Django to use "Toppings"
        # when it needs to refer to more than one topping
        verbose_name_plural = "Toppings"

    def __str__(self):
        return f"{self.name[:50]}..."
