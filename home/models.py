from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='')
    upload_user = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.upload_user}, {self.uploaded_at}'