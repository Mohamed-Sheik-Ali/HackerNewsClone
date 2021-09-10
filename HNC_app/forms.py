from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# To create a signin form
class CreateUserForm(UserCreationForm):
    # Meta class is used to change the behaviour of model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']