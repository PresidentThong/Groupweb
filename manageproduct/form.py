from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "name",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter description...",
                    "id": "description",
                },
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = "__all__"

        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter code...",
                    "id": "code",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter description...",
                    "id": "description",
                },
            ),
            "name_pro": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter Vietnamese name...",
                    "id": "name_vi",
                },
            ),
    
            "input_date": forms.TimeInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter credit...",
                    "id": "credit",
                },
            ),
            "out_date": forms.TimeInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter hour...",
                    "id": "hour",
                },
            ),
            "category_id": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "category_id",
                },
            ),
        }
