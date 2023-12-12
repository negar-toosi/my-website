from django.contrib import admin
from mysite.models import content,newsletter
# Register your models here.

class contentAdmin(admin.ModelAdmin):
    list_display = ('name','email')
admin.site.register(content,contentAdmin)
admin.site.register(newsletter)