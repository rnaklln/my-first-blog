from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'header_image']
        widgets = {
            'text': CKEditorWidget(),
        }
