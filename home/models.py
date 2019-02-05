from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='',
                            validators=[FileExtensionValidator(allowed_extensions=settings.CONTENT_TYPES)])
    comment = models.TextField(max_length=150,
                                null=True)
    ip_address = models.TextField(max_length=15,
                               null=True)
    upload_user = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.upload_user}, {self.uploaded_at}'