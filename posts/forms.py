from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий',
                'rows': 4
            })
        }
        labels = {
            'author': 'Имя',
            'content': 'Комментарий'
        }
