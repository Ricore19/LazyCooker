"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import AdminMessage, Categori
from .forms import NewCategorie

def administration(request):
    return render(request, "admin/administration.html")


def adminmessage(request):
    messagelist = AdminMessage.objects.all()
    return render(request, "admin/adminmessage.html", locals())


def admindeletmessage(request, identifiant):
    message = AdminMessage.objects.get(id=identifiant)
    message.delete()
    return redirect("http://localhost:8080/administration/message/")


def admincategori(request):
    categorilist = Categori.objects.all()
    error = False
    ok = False

    if request.method == "POST":
        form = NewCategorie(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            contenu = form.cleaned_data["contenu"]

            cat = Categori()
            cat.titre = titre
            cat.contenu = contenu
            cat.save()

            ok = True

        else:
            error = True
    else:
        form = NewCategorie()

    return render(request, "admin/admincategrori.html", locals())


def admindeletcategori(request, identifiant):
    categori = Categori.objects.get(id=identifiant)
    categori.delete()
    return redirect("http://localhost:8080/administration/categori/")
"""