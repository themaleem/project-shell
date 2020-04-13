from django.contrib import admin
from .models import (
    Profile,
    Draft,
    Post,
    Response
)
# Register your models here.

class ResponseInline(admin.TabularInline):
    model = Response
    extra = 2

class PostAdmin(admin.ModelAdmin):
    list_display = ( 
        'body',
        )
    fieldsets =  [
        (
            None, 
            {
                'fields': [
                    'title',
                    'body',
                    'owner'
                    ]
                }
            ),
        ]
    inlines = [ResponseInline]

admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(Draft)
admin.site.register(Response)