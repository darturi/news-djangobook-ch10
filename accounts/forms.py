from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# This form is to interact with the CustomUser model as a user creating an
# account
class CustomUserCreationForm(UserCreationForm):
    # using the Meta class allows us to override the default usage of the
    # User class as the model
    class Meta:
        model = CustomUser
        # for fields we set the value as all the fields that would normally
        # come with the use of the defualt user class + the age field
        fields = (
            "username",
            "email",
            "age",
        )


# This form is to interact with the CustomUser model in the context of changing
# a user account from the admin dash
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
