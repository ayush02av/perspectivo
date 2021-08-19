from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(WorkType)
admin.site.register(Work)
admin.site.register(Review)