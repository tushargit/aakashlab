from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coordinator(models.Model):
    """Aakash Coordinators.
    """
    user = models.OneToOneField(User)

    # Addition info
    contact = models.IntegerField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username


class AakashCenter(models.Model):
    """Aakash centers.
    """
    ac_id = models.IntegerField(max_length=6, unique=True)
    quantity = models.IntegerField(max_length=7, default=0)
    name = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    coordinator = models.OneToOneField(Coordinator)
    active = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

        
class TeamMember(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

        
class Mentor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return self.name

        
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ac = models.ForeignKey(AakashCenter)
    summary = models.TextField(max_length=500, unique=True)
    member = models.ManyToManyField(TeamMember)
    mentor = models.ManyToManyField(Mentor)
    src_url = models.URLField()
    doc_url = models.URLField()
    apk = models.FileField(upload_to='apk')
    logo = models.ImageField(upload_to='project_logo', blank=True)
    download_count = models.IntegerField(default=0)
    date_uploaded = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name        


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)

    def __unicode__(self):
        return self.email
