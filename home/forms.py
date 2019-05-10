from django import forms

# class Commentform(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     email = forms.EmailField(label='Your email')
#     message = forms.CharField(label='What\'s on your mind', widget=forms.Textarea())


from django.forms import ModelForm
from .models import Comments

class Commentform(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'message']
        
