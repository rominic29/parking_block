from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _

from .models import User


class SignUpForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'password1',
            'password2',
            'email',
        }

        labels = {
            'password1': _('Password'),
            'password2': _('Confirm Password'),
            'email': _('Email'),
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = user.email
        if commit:
            user.save()
        return user
