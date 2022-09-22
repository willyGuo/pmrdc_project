from django.contrib import admin
from myapp.models import student, requisition,clereply_db, NewsUnit
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter =('cName', 'cSex')
    search_fields = ('cName',)
    ordering =('id',)

class requisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName','cNumber', 'cdatestart','cFunction','cdateend','cProjectname', 'cCusetername', 'cProjectcode',\
         'cLocation', 'cContent', 'cSchedule','cSpecial',\
        'cLastproject', 'cType', 'cCotpye','cProjecttype', 'cStage', 'cNoted', 'title', 'uploadedFile', 'dateTimeOfUpload', 'cStatus')
    list_filter =('cName', )
    search_fields = ('cName',)
    ordering =('id',)
class clereply_dbAdmin(admin.ModelAdmin):
    list_display = ('product', 'checklist', 'producttype', 'productscoreline')
    list_filter =('product', 'checklist')
    search_fields = ('product',)
    ordering =('id',)

class NewsUnit_dbAdmin(admin.ModelAdmin):
    list_display = ('catego', 'nickname', 'title', 'message', 'pubtime', 'enabled', 'press')
    list_filter =('catego', 'nickname')
    search_fields = ('catego',)
    ordering =('id',)


admin.site.register(student,studentAdmin)
admin.site.register(requisition,requisitionAdmin)
admin.site.register(clereply_db,clereply_dbAdmin)
admin.site.register(NewsUnit,NewsUnit_dbAdmin)