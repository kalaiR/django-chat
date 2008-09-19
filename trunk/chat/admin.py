#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display=('date','user', 'summary',)
    list_filter = ('user',)
admin.site.register(Post, PostAdmin)
