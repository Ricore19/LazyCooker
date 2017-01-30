from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import NewAdminMessage
from .models import AdminMessage


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    error = False
    ok = False
    if request.method == "POST":
        form = NewAdminMessage(request.POST)
        if form.is_valid():

            adminMSG = AdminMessage()
            adminMSG.auteur = request.user
            adminMSG.titre = form.cleaned_data["titre"]
            adminMSG.contenu = form.cleaned_data["contenu"]
            adminMSG.save()

            ok = True
        else:
            error = True
    else:
        form = NewAdminMessage()

    return render(request, "contact.html", locals())


