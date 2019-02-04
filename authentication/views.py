from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

def index(request):
    if request.user.is_authenticated :
        return redirect('/home/')

    return render(request, 'index.html', context={})

def logout_view(request):
    auth_logout(request)
    return redirect('/')