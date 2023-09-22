from django.contrib import admin
from app.models import JobPost, Location, Authors, Skills

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'creation_date')
    list_filter = ('creation_date', 'salary', 'title')
    search_fields = ('title', )
    search_help_text = "Write Your Query Here and Enter"
    # fields = (('title', 'description'), 'expiry_date')
    # exclude = ('slug',)
    fieldsets = ( 
                 (
                     'Basic Information', { 
                                'fields': ('title', 'description')
                                }
                 ), 
                 (
                     'More Information', { 
                                          'classes': ('collapse', 'wide'),
                                          'fields': (('salary', 'expiry_date'), 'slug')
                                        }
                 ), 
    )


admin.site.register(JobPost, )
admin.site.register(Location)
admin.site.register(Authors)
admin.site.register(Skills)


