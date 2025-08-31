from django import forms
from shop.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

    # category_name = forms.CharField(
    #     widget=forms.TextInput(attrs={'required': 'required'}),
    #     label='Category Name' 
    # )
