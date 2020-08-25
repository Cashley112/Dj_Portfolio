from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "registration/login.html")

def pw_change(request):
    return render(request, "registration/password_change_form.html")

def password_reset_form(request):
    return render(request, "registration/password_reset_form.html")