from django.forms import ModelForm
from home.models import Document

class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ('upload',)