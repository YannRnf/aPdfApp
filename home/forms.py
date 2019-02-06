from django.forms import ModelForm
from home.models import Document
from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

# DocumentForm Class definition
class DocumentForm(ModelForm):
    # Small customisation of the html generated fields.
    # Comment isn't required for the form submission and 
    # add the bootstrap class for shiny look
    comment = forms.CharField(  required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Write your comment here'}
                                )
                            )
    # Add the bootstrap form class for shiny look.
    # Add client-side file extension verification, 
    # but that more to avoid the user error than a security
    upload = forms.FileField( widget=forms.FileInput(
                                attrs={
                                    'accept' : "application/pdf",
                                    'class': 'form-control-file',
                                    'style': 'text-align:center'
                                }
                                )
                            )
    # Clean override method will call the check_file method designed 
    # for the file size "backend-side" validation
    def clean(self):
        self.check_file()
        return self.cleaned_data
    # Check_file method designed for the file size "backend-side" validation
    def check_file(self):
        # Retrieve the file content
        content = self.cleaned_data["upload"]
        # Simply compare to our env variable for the pdf file size
        if content.size > int(settings.MAX_UPLOAD_SIZE):
            # Raise the error if the file is too big
            raise forms.ValidationError(_("Please keep file size under %s. Current file size %s")%(filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content.size)))
        return content

    # Meta class for specifying the underlying class (here : Document), 
    # and list the fields for the html generation of the form's fields
    class Meta:
        model = Document
        fields = ('upload', 'comment')