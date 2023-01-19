from django.db import models

# Create your models here.
class URL_NOOPENER(models.Model):
    source_url=models.CharField(max_length=250)
    target_url=models.CharField(max_length=250)
    links=models.CharField(max_length=250)
    noopener = models.CharField(max_length=45,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)

class URL(models.Model):
    source_url=models.CharField(max_length=250)
    target_url=models.CharField(max_length=250)
    links=models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)    


class Celery_URL_NOOPENER(models.Model):
    source_url=models.CharField(max_length=250)
    target_url=models.CharField(max_length=250)
    links=models.CharField(max_length=250)
    noopener = models.CharField(max_length=45,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)

class Celery_URL(models.Model):
    source_url=models.CharField(max_length=250)
    target_url=models.CharField(max_length=250)
    links=models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)  