from django import forms

from .models import Pizza, Topping, Comment

# define a class called PizzaForm, which inherits from forms.ModelForm
class PizzaForm(forms.ModelForm):
    # Meta class is the simplest vsersion of a ModelForm
    # tells django which model to base the form on and which fields to include in the form
    class Meta:
        model = Pizza
        fields = ["name"]
        labels = {"name": ""}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["name"]
        labels = {"name": ""}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name"]
        labels = {"name": ""}
