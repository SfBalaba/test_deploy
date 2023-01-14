from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser

from .models import Buyer


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer
        fields = UserCreationForm.Meta.fields + ("email", )
