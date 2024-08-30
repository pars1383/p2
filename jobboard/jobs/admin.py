from django.contrib import admin
from .models import JobAd, JobApplication, Employer, JobSeeker

admin.site.register(JobAd)
admin.site.register(JobApplication)
admin.site.register(Employer)
admin.site.register(JobSeeker)
