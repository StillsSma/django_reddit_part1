
from django import forms
from app.models import Subreddit


class SubForm(forms.ModelForm):

    class Meta:
        fields = ("name", "description" )
        model = Subreddit
