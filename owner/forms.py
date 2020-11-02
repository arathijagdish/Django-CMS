from django.forms import forms, ModelForm, TextInput, Textarea
from .models import Post

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('created_by',)

        widgets = {
            'title':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body':Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description':Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'slug':TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }