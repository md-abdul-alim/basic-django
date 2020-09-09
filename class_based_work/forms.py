from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(label='',
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Robust Product Title"
                                }
                            )
                        )
    content = forms.CharField()
    active = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
