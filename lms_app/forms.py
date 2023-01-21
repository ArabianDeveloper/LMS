from django import forms
from .models import Book , Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }

widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'author': forms.TextInput(attrs = {'class':'form-control'}),
            'pages': forms.NumberInput(attrs = {'class':'form-control'}),
            'photo_book': forms.FileInput(attrs = {'class':'form-control'}),
            'photo_author': forms.FileInput(attrs = {'class':'form-control'}),
            'price': forms.NumberInput(attrs = {'class':'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class':'form-control'}),
        }
class BookForm(forms.ModelForm):
    title = forms.CharField(label='عنوان الكتاب' , widget= widgets['title'])
    author = forms.CharField(label='مؤلف الكتاب' , widget= widgets['author'])
    pages = forms.IntegerField(label='عدد الصفحات' , widget= widgets['pages'])
    # category = forms.TypedChoiceField(label='الفئة' , widget= widgets['category'])
    # status = forms.ChoiceField(label='الحالة' , widget= widgets['status'])
    pdf_file = forms.FileField(label='الكتاب' , widget= widgets['pdf_file'] , allow_empty_file=True)
    photo_book = forms.ImageField(label='صورة الكتاب' , widget= widgets['photo_book'])
    photo_author = forms.ImageField(label='صورة المؤلف' , widget= widgets['photo_author'])
    price = forms.FloatField(label='السعر' , widget= widgets['price'])
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['title' , 'author' , 'pages' , 'category' , 'status' ,'pdf_file', 'photo_book' , 'photo_author' , 'price' , 'retal_price_day' , 'retal_period' , 'total_rental' , 'Discription']
        widgets = {
            'category': forms.Select(attrs = {'class':'form-control'}),
            'status': forms.Select(attrs = {'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs = {'class':'form-control', 'id':'rentalprice'}),
            'total_rental': forms.NumberInput(attrs={'class':'form-control', 'id':'rentaldays'}), 
            'retal_period': forms.NumberInput(attrs = {'class':'form-control', 'id':'totalrental'}),
            'Discription': forms.Textarea(attrs={'class':'form-control'}),
        }
        
