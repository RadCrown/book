from django.forms import ModelForm

from .models import by_rubric
class BbForm(ModelForm):
    class Meta:
        model = BbFormfields = {'title', 'content', 'price', 'rubric'}