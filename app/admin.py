from django.contrib import admin
from app.models import JobPost

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'creation_date')
    list_filter = ('creation_date', 'salary', 'title')


admin.site.register(JobPost, JobAdmin)
