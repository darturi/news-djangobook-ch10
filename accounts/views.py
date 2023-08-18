from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # what form is being 'viewed'
    success_url = reverse_lazy("login")  # where successful input takes you
    template_name = "registration/signup.html"  # where template is stored
