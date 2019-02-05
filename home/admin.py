from django.contrib import admin
from home.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('upload', 'upload_user', 'ip_address', 'uploaded_at', 'comment')