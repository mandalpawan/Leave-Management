from django.contrib import admin
from .models import applyleave
from .models import leavetype
from managementsystem.models import college

# Register your models here.
admin.site.register(applyleave),
admin.site.register(leavetype),
admin.site.register(college),