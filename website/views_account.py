from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, "account/login.html", locals())


def deconnexion(request):
    logout(request)
    return render(request, "account/logout.html")


def subscription(request):
    error = False

    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            firstname = form.cleaned_data["firstname"]
            secondname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]

            if password == password2:
                user = User.objects.create_user(username, email, password, first_name=firstname, last_name=secondname)
                if user:
                    login(request, user)
                else:
                    error = True
            else:
                error = True
        else:
            error = True
    else:
        form = SubscriptionForm()

    return render(request, "account/subscription.html", locals())


def profile(request, name):

    viewuser = User.objects.get_by_natural_key(name)
    messages = Message.objects.filter(destinataire=viewuser)
    posts = Post.objects.filter(auteur=viewuser)
    return render(request, "account/profile.html", locals())


def changeprofile(request):
    error = False
    ok = False

    if request.method == "POST":
        form = ChangeProfile(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]

            request.user.first_name = firstname
            request.user.last_name = lastname
            request.user.email = email

            request.user.save()

            ok = True
        else:
            error = True
    else:
        form = ChangeProfile()

    return render(request, "account/changeprofile.html", locals())


def changepassword(request):
    error = False
    ok = False

    if request.method == "POST":
        form = ChangePassword(request.POST)
        if form.is_valid():
            password0 = form.cleaned_data["password0"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]

            if request.user.check_password(password0) and password == password2:
                request.user.set_password(password)
                request.user.save()
                ok = True
            else:
                error = True
        else:
            error = True
    else:
        form = ChangePassword()

    return render(request, "account/changepassword.html", locals())


def message(request, name):
    error = False
    ok = False

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            contenu = form.cleaned_data["contenu"]

            lol = Message()
            lol.titre = titre
            lol.contenu = contenu
            lol.destinataire = User.objects.get_by_natural_key(name)
            lol.auteur = request.user
            lol.save()

            ok = True

        else:
            error = False

    else:
        form = MessageForm()

    return render(request, "account/message.html", locals())


def delmessage(request, name, ide):
    messages = Message.objects.get(id=ide)
    if request.user == messages.destinataire:
        messages.delete()
        return redirect("../")
