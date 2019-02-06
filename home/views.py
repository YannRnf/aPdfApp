from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.forms import DocumentForm
from home.models import Document

# index route for the "home" page, users MUST be logged in to access (redirection to "/"" neither)
@login_required(login_url='/')
def index(request):
    # Retrieval of the current logged user
    connectedUser = request.user
    # initialization of an error variable
    error = None

    # Handle the received POST
    if request.method == 'POST':
        # Instanciate the DocumentForm class with received data
        form = DocumentForm(request.POST,request.FILES)
        # Form validation (MUST be reworked for extention files)
        if form.is_valid():
            # Saving the object without commiting to DB
            obj = form.save(commit=False)

            # IP retrieval, first from the X_FORWARDED_FOR and then the REMOTE_ADDR if the first isn't set
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            # Add the address AND linking the connected user for the foreignKey
            obj.ip_address = ipaddress
            obj.upload_user = connectedUser
            # Saving to DB
            obj.save()
        else :
            # Handle the form errors if !form.is_valid()
            error = form.errors

    # New DocumentForm instance
    form = DocumentForm()
    # Load the user's own documents
    documents = Document.objects.filter(upload_user=connectedUser)

    # Render the home view with the form, documents list, user and potential errors
    return render(request, 'home.html', context={
        'form': form,
        'documents' : documents,
        'user' : connectedUser,
        'error': error
    })