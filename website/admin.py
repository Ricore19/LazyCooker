from django.contrib import admin
from .models import *


class AdminMessageAdmin(admin.ModelAdmin):
    list_display = ("titre", "contenu", "auteur", "date")
    ordering = ("-date",)

class LikeAdmin(admin.ModelAdmin):
    list_display = ("auteur", "post")
    ordering = ("-auteur",)

admin.site.register(AdminMessage, AdminMessageAdmin)
admin.site.register(Message)
admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Like, LikeAdmin)
