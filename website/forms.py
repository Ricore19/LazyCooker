from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class SubscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    firstname = forms.CharField(label="Prénom", max_length=30)
    lastname = forms.CharField(label="Nom", max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class ChangeProfile(forms.Form):
    firstname = forms.CharField(label="Prénom", max_length=30)
    lastname = forms.CharField(label="Nom", max_length=30)
    email = forms.EmailField()


class ChangePassword(forms.Form):
    password0 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class NewCategorie(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)


class NewAdminMessage(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)


class MessageForm(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    contenu = forms.CharField(widget=forms.Textarea)


class PostForm(forms.Form):
    titre = forms.CharField(label="Titre", max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)
