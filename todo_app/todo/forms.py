from django import forms

class TodoNewForm(forms.Form):
  title = forms.CharField(max_length=128)