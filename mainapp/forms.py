from django import forms

from mainapp.services import event


class LinkForm(forms.Form):
    link = forms.URLField(required=True)
    
    def clean(self, *args, **kwargs):
        instance = super().clean(*args, **kwargs)
        event(instance.get("link"))
        return instance
