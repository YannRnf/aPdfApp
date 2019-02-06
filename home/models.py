from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Document class definition
class Document(models.Model):
    # Upload DateTime
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # File with the native Django FileExtensionValidator
    upload = models.FileField(upload_to='',
                            validators=[FileExtensionValidator(allowed_extensions=settings.CONTENT_TYPES)])
    # Eventual comment
    comment = models.TextField(max_length=150,
                                null=True)
    # IP address during upload of the doc 
    ip_address = models.TextField(max_length=15,
                               null=True)
    # User can have multiple document, and a Document has only one Owner, so it's a ForeignKey
    # On deletion, we set to NULL, but we could have CASCADE it.
    upload_user = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True)
    # To string definition for debugging purposes
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.upload_user}, {self.uploaded_at}'