from django.contrib import admin
from blog.models import Post, Category, Comments 
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
@admin.register(Comments)    
class CommentsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ('name','post')
    
admin.register(Comments, CommentsAdmin)
admin.site.register(Category)
admin.site.register(Post, postAdmin)