from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from home.forms import DocumentForm
from home.models import Document

@login_required(login_url='/')
def index(request):
    connectedUser = request.user
    error = None

    if request.method == 'POST':
        form = DocumentForm(None,request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            
            obj.ip_address = ipaddress
            obj.upload_user = connectedUser
            obj.save()
        else :
            error = form.errors

    form = DocumentForm()
    documents = Document.objects.filter(upload_user=connectedUser)

    return render(request, 'home.html', context={
        'form': form,
        'documents' : documents,
        'user' : connectedUser,
        'error': error
    })