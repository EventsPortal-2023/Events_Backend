from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Events)
admin.site.register(EventLikes)
admin.site.register(Photo)
admin.site.register(Favourite)