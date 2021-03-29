from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect


# password for admin is Fzee07***000$$$
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        # messages.warning(request, 'You are not Authenticated, Please Try Again.')
        return redirect("/login")

    return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        # Check if user has entered correct credentials
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('/')
        # A backend authenticated the credentials
        else:
            return render(request, 'login.html')

    # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
