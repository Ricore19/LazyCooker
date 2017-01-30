from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core.paginator import Paginator


def forumsection(request):
    sections = Section.objects.all()
    return render(request, "forum/section.html", locals())


def forumpost(request, ids, page):
    sections = Section.objects.get(id=ids)
    posts = Post.objects.filter(section=sections).order_by("-dateactive")

    pagination = Paginator(posts, 5)
    paginationpage = pagination.page(page)
    previous = paginationpage.has_previous()
    nexts = paginationpage.has_next()
    pageprevious = int(page) - 1
    pagenext = int(page) + 1

    return render(request, "forum/post.html", locals())


def forumpostdetail(request, idp, page):
    posts = Post.objects.get(id=idp)
    sections = posts.section
    comments = Comment.objects.filter(post=posts)

    pagination = Paginator(comments, 10)
    paginationpage = pagination.page(page)
    previous = paginationpage.has_previous()
    nexts = paginationpage.has_next()
    pageprevious = int(page) - 1
    pagenext = int(page) + 1

    posts.shows = posts.shows + 1
    posts.save()

    if request.user.is_staff:
        like = Like.objects.filter(auteur=request.user, post=posts)

    error = False
    ok = False

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            contenu = form.cleaned_data["contenu"]

            lol = Comment()
            lol.auteur = request.user
            lol.contenu = contenu
            lol.post = posts
            lol.save()

            posts.dateactive = timezone.now()
            posts.save()
            ok = True
        else:
            error = True
    else:
        form = CommentForm()

    return render(request, "forum/postdetail.html", locals())


def forumpostlike(request, idp, page):

    if request.user.is_authenticated:
        posts = Post.objects.get(id=idp)
        posts.likes = posts.likes + 1
        posts.shows = posts.shows - 1
        posts.save()

        like = Like()
        like.post = posts
        like.auteur = request.user

        like.save()

    return redirect("../")


def forumpostdislike(request, idp, page):
    if request.user.is_authenticated:
        posts = Post.objects.get(id=idp)
        posts.likes = posts.likes - 1
        posts.shows = posts.shows - 1
        posts.save()

        like = Like.objects.filter(auteur=request.user, post=posts)
        if like:
            like.delete()

    return redirect("../")


def forumpostdelcomment(request, idp, page, idc):

    if request.user.is_authenticated:
        comments = Comment.objects.get(id=idc)
        posts = comments.post
        idp = posts.id

        if request.user == comments.auteur or request.user == posts.auteur or request.user.is_staff:
            comments.delete()
            posts.shows = posts.shows - 1
            posts.save()

            return redirect("../../")


def forumpostdel(request, idp):

    if request.user.is_authenticated:
        posts = Post.objects.get(id=idp)

        if posts.auteur == request.user or request.user.is_staff:
            posts.delete()

    return redirect("/forum")


def forumpostcreate(request, ids):
    error = False
    ok = False

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            contenu = form.cleaned_data["contenu"]

            sections = Section.objects.get(id=ids)

            posts = Post()
            posts.titre = titre
            posts.contenu = contenu
            posts.auteur = request.user
            posts.section = sections

            posts.save()

            ok = True

        else:
            error = True

    else:
        form = PostForm()

    return render(request, "forum/postcreate.html", locals())
