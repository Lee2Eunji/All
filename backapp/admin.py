from django.contrib import admin

# Register your models here.
from .models import Developer, Question, Choice

admin.site.register(Developer)
admin.site.register(Question)
admin.site.register(Choice)