from django.contrib.auth.models import User

from allauth.account.forms import SignupForm

from django.views.generic.edit import CreateView


class SignView(CreateView):
    model = User
    form_class = SignupForm
    success_url = '/adverts/'
