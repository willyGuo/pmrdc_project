from django.contrib import admin
from myapp.models import student, requisition
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter =('cName', 'cSex')
    search_fields = ('cName',)
    ordering =('id',)

class requisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName','cNumber', 'cdatestart','cFunction','cdateend','cProjectname', 'cCusetername', 'cProjectcode',\
         'cLocation', 'cContent', 'cSchedule','cSpecial',\
        'cLastproject', 'cType', 'cCotpye','cProjecttype', 'cStage', 'cNoted', 'title', 'uploadedFile', 'dateTimeOfUpload')
    list_filter =('cName', )
    search_fields = ('cName',)
    ordering =('id',)

admin.site.register(student,studentAdmin)
admin.site.register(requisition,requisitionAdmin)
