from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

# Index method, default route
def index(request):
    # For the user ease, we redirect all connected user to the home page
    if request.user.is_authenticated :
        return redirect('/home/')
    # For the others, we render the index page
    return render(request, 'index.html', context={})

# Logout route
def logout_view(request):
    # Native Django logout
    auth_logout(request)
    # Redirect to the default route
    return redirect('/')