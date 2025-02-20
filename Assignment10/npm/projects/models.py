from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):

    email = models.EmailField(max_length=254)
    title = models.CharField( max_length= 70)
    desc = models.CharField(max_length=700,blank=True,null=True)
    enroll_no = models.IntegerField()
    year = models.CharField( max_length=1)
    sec = models.CharField( max_length=1)
    git_link = models.CharField(max_length=70)
    live_link = models.CharField(max_length=70,blank=True,null=True)
    screenshot = models.ImageField( upload_to="projects/images",blank=True,null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_on = models.DateField(auto_now_add=True)
    updated_on =models.DateField(auto_now=True)


    def __str__(self):
        return self.title + " | " + str(self.submitted_by)

    class Meta:
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'