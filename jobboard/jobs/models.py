from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()

class JobAd(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='job_photos/', blank=True, null=True)
    validity_date = models.DateField()
    job_category = models.CharField(max_length=100)
    job_rights = models.TextField()
    working_hours = models.CharField(max_length=50)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class JobApplication(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job_ad = models.ForeignKey(JobAd, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
