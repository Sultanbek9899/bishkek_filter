from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(max_value=20, min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ListCartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)