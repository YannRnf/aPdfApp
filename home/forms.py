from django.forms import ModelForm
from home.models import Document
from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class DocumentForm(ModelForm):
    comment = forms.CharField( widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Write your comment here'
                                }
                                ))
    upload = forms.FileField( widget=forms.FileInput(
                                attrs={
                                    'class': 'form-control-file',
                                    'style': 'text-align:center'
                                }
                                ))

    def clean(self):
        self.check_file()
        return self.cleaned_data
    
    def check_file(self):
        content = self.cleaned_data["upload"]
        if content.size > int(settings.MAX_UPLOAD_SIZE):
            raise forms.ValidationError(_("Please keep file size under %s. Current file size %s")%(filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content.size)))
        return content

    class Meta:
        model = Document
        fields = ('upload', 'comment')