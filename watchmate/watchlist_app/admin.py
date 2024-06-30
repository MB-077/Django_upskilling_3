from django.contrib import admin

# Register your models here.

from .models import *

# V1
# admin.site.register(Movie)

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)