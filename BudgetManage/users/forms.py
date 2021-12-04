from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import CharField, Textarea

from users.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']

    goal = CharField(
        label='What is your goal for saving', widget=Textarea, min_length=40
    )

    def save(self, commit=True):
        self.instance.is_active = False
        new_user = super().save(commit)

        # We should assign Customers group permission
        
        goal = self.cleaned_data['goal']
        profile = Profile(goal=goal, user=new_user)
        if commit:
            profile.save()
        return new_user
