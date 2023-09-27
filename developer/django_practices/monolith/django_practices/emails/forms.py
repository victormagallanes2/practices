from django import forms


class EmailForm(forms.Form):
    
    to = forms.EmailField()
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)