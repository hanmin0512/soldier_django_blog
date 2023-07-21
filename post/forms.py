from django.forms import inlineformset_factory
from post.models import Post, IMG
from django import forms

PostInlineFormset = inlineformset_factory(Post, IMG,
                                         fields=['image'],
                                          extra=1 )

class PSH(forms.Form):
    search_word = forms.CharField(label='Search Post')
