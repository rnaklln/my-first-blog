from django.contrib import admin
from .models import Post
from django.contrib.sites.models import Site

admin.site.register(Post)
admin.site.register(Site)
