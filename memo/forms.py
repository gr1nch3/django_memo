from django.contrib.auth.forms import UserCreationForm

from .models import MemoUser


# ---------------------------------------------------------------------------- #
#                   creating a form to allow users to sign up                  #
# ---------------------------------------------------------------------------- #

# ----------------------------- USer signup form ----------------------------- #
class UserCreation(UserCreationForm):
    class Meta:
        model = MemoUser
        fields = ('username',)

    def save(self, commit=True):
        user = super(UserCreation, self).save(commit=False)
        if commit:
            user.is_active = True
            user.save()

        return user