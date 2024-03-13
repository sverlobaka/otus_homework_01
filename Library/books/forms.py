from django import forms

from .models import Book, Author, Genre, Reader, BookIssuanceAccounting, CopyBook


class BookForm(forms.ModelForm):
    name = forms.CharField(label="Название книги")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Имя автора книги")
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label="Жанр книги")
    description = forms.CharField(widget=forms.Textarea, label="Описание")

    class Meta:
        model = Book
        fields = "__all__"


class ReaderForm(forms.ModelForm):
    name = forms.CharField(label="Имя читателя")
    address = forms.CharField(label="Адрес читателя")
    email = forms.CharField(label="Электронная почта читателя")

    class Meta:
        model = Reader
        fields = "__all__"


class BookIssuanceAccountingForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Наименование книги")
    copy_book = forms.ModelChoiceField(queryset=CopyBook.objects.all(), label="Инвентарный номер книги")
    reader = forms.ModelChoiceField(queryset=Reader.objects.all(), label="Кому выдается книга")
    return_date = forms.DateField(label="Дата возврата книги")
    # return_book = forms.BooleanField(label="Возвращена")

    class Meta:
        model = BookIssuanceAccounting
        fields = "__all__"