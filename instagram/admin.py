# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Image,Comment,Like
# from .models import photos

# Register your models here.
admin.site.register(Image)
# admin.site.register(photos)
admin.site.register(Comment)
admin.site.register(Like)