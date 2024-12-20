from django.contrib import admin
from .models import *

# Register your models here.

class InternshipAdmin(admin.ModelAdmin):
    list_display = (
    'fullname',
    'usn',
    'email',
    'college_name',
    'offer_status',
    'start_date',
    'end_date',
    'project_report',
    'timeStamp')
    search_fields=('fullname','usn','email')
    list_filter=['college_name','project_report','offer_status']

admin.site.register(Internship,InternshipAdmin)
admin.site.register(Blogs)
