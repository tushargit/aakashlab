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


class AakashCentre(models.Model):
    """Aakash centres.
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

        
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ac = models.ForeignKey(AakashCentre)
    summary = models.TextField(max_length=500, unique=True)
    src_url = models.URLField(blank=True)
    doc_url = models.URLField(blank=True)
    doc_file = models.FileField(upload_to='docs', blank=True)
    apk = models.FileField(upload_to='apk')
    additional_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to='project_logo', blank=True)
    download_count = models.IntegerField(default=0)
    date_uploaded = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name        


class TeamMember(models.Model):
    member_name = models.CharField(max_length=200)
    member_email = models.EmailField(blank=True)
    member_project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.member_name


class Mentor(models.Model):
    mentor_name = models.CharField(max_length=200)
    mentor_email = models.EmailField(blank=True)
    mentor_project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.mentor_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)

    def __unicode__(self):
        return self.email


class Faq(models.Model):
    """FAQs"""
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.question


class Pub(models.Model):
    """Publications and articles related to Aakash.
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    url = models.URLField(blank=True)
    attachment = models.FileField(upload_to='pubs', blank=True)
    
    def __unicode__(self):
        return self.title
        
        

