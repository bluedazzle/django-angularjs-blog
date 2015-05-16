from django.contrib import admin

from app.blog_log.models import *

# Register your models here.

class BackLogAdmin(admin.ModelAdmin):
    list_display = ('content', 'create_time', 'modify_time')
    list_filter = ('modify_time',)
    ordering = ('-modify_time',)

admin.site.register(AccIP)
admin.site.register(ReqRecord)
admin.site.register(BackLog, BackLogAdmin)