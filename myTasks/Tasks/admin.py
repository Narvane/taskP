from django.contrib import admin
from .models import Task, Author
# Register your models here.

admin.site.register(Task)
admin.site.register(Author)