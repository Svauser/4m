from django import forms

from post.models import Product,Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите заголовок'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите текст'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите цену'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'price': 'Цена',
            'tags': 'Тэги',
            'category': 'Категория'
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Введите текст'
                }
            )
        }
        labels = {'text':'Текст'}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

