from django import forms
from .models import Product
# step 1


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='',
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Product Title"
                                }
                            )
                            )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 8,
                "col": 150
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    summary = forms.CharField(required=True)


class robust_ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Robust Product Title"
                                }
                            )
                            )
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 8,
                "col": 150
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    summary = forms.CharField(required=True, initial="robust summary")

    class Meta:
        model = Product
        fields = [
            'title',
            'email',
            'description',
            'price',
            'summary',
            'featured'
        ]
    # optional validation
    '''
    def clean_title(self,*args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "ABC" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "EFG" in title:
            raise forms.ValidationError("This is not a valid titel")
        return title
    '''

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("com"):
            raise forms.ValidationError("This is not a valid email")
        return email
