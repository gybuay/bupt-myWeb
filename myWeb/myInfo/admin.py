from django.contrib import admin
from .models import *
# Register your models here.

class ExamInfoShow(admin.ModelAdmin):
    list_display = ['id','title','content']

class AdminShow(admin.ModelAdmin):
    list_display = ['id','name','p_id','p_class']

admin.site.register(ExamInfo,ExamInfoShow)
admin.site.register(Admin,AdminShow)
