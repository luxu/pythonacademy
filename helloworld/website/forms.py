from helloworld.models import Comercio, Gasto
from django import forms

# FORMULÁRIO DE INCLUSÃO DE COMÉRCIOS
# -------------------------------------------

class InsereComercioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Comercio

        # Campos que estarão no form
        fields = [
            'name',
            'slug'
        ]

# FORMULÁRIO DE INCLUSÃO DE GASTOS
# -------------------------------------------

class InsereGastoForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Gasto

        # Campos que estarão no form
        fields = [
            'name',
            'slug',
            'valor',
            'datagasto',
            'comercio'
        ]
