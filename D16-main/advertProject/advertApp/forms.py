from django import forms

from .models import Advert, Response


class CreateAdvertForm(forms.ModelForm):
    category = forms.ChoiceField(label="Категория", choices=Advert.CATEGORY, widget=forms.Select(attrs={"style": "width:100%"}))
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"style": "width:100%"}))
    file = forms.FileField(label="", required=False)

    class Meta:
        model = Advert
        fields = ['category', 'text', 'file']


class CreateResponseForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"style": "width:100%"}))

    class Meta:
        model = Response
        fields = ['text']
