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
        # TODO : Add FILE VERIFICATIONS
        form = DocumentForm(None,request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
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