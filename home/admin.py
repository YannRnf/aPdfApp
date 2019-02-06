from django.contrib import admin
from home.models import Document

# Admin customization, adding our custom Document class to the native Django interface
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    # List the informations we want to show to the admin
    list_display = ('upload', 'upload_user', 'ip_address', 'uploaded_at', 'comment')