from django import forms

class UploadFileForm(forms.Form):
  titolo = forms.CharField(required=False)
  file=forms.FileField()
  add_comment1 = forms.BooleanField(required=False, label="Aggiungi commento 1")
  add_comment2 = forms.BooleanField(required=False, label="Aggiungi commento 2")