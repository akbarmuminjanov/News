from django import forms
from .models import News, Category

# CATEGORY_CHOICES = []
# for cat in Category.objects.all():
#     CATEGORY_CHOICES.append((cat.id, cat.titele))

class NewsForm (forms.ModelForm):
    titele = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'yangilik nomi'
    }))
    mazmuni = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'yangilik mazmini'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
    }))
    # category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = News
        fields = ["titele", "mazmuni", "image", "category"]

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs["class"] = "form-select"
        self.fields['category'].widget.attrs["style"] = "width: 300px"




class CategoryForm(forms.ModelForm):
    titele = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'kategoriya nomi'
    }))
    mazmuni = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'kategoriya mazmini'
    }),required=False)
    class Meta:
        model = Category
        fields = ["titele", "mazmuni"]
   



