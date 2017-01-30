from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AdminMessage(models.Model):
    auteur = models.ForeignKey(User)
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre


class Message(models.Model):
    auteur = models.ForeignKey(User, related_name="auteur")
    destinataire = models.ForeignKey(User, related_name="destinataire")
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre


class Section(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)

    def __str__(self):
        return self.titre


class Post(models.Model):
    auteur = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    dateactive = models.DateTimeField(default=timezone.now, verbose_name="Date d'activité")
    likes = models.IntegerField(default=0)
    shows = models.IntegerField(default=0)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    auteur = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")


class Like(models.Model):
    auteur = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class Ingredient(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Recipe(models.Model):
    titre = models.CharField(max_length=100)
    official = models.BooleanField(default=False)
    image = models.FilePathField(default="img/recipe/none.jpg")
    youtube = models.URLField(default="http://www.youtube.com/")
    ingredient = models.ManyToManyField(Ingredient)
    temps = models.FloatField()
    cout = models.FloatField()
    description = models.TextField(null=True)
    besoin = models.TextField(null=True)
    contenu = models.TextField(null=True)

    def __str__(self):
        return self.titre
