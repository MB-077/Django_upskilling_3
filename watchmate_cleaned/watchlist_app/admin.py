from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)