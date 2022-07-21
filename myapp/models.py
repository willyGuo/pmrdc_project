from django.db import models
from myapp.formatChecker import ContentTypeRestrictedFileField
from django.core.exceptions import ValidationError

# Create your models here.
class student(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateTimeField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.cNumber, filename)

class requisition(models.Model):
    cName = models.CharField(max_length=20, default="")
    cNumber = models.CharField(max_length=20, default="")
    cCusetername = models.CharField(max_length=20, null=False)
    cProjectname = models.CharField(max_length=20, null=False)
    cProjectcode = models.CharField(max_length=20, null=False)
    cLocation = models.CharField(max_length=100, default='')
    cContent = models.CharField(max_length=100, default='')
    cLastproject = models.CharField(max_length=100, default='')
    cType = models.CharField(max_length=100, default='')
    cCotpye = models.CharField(max_length=100, default='')
    cProjecttype = models.CharField(max_length=100, default='')
    cStage = models.CharField(max_length=100, default='')
    cNoted = models.CharField(max_length=100,default='')
    cSchedule = models.CharField(max_length=100,default='')
    cSpecial = models.CharField(max_length=100,default='')
    cdatestart = models.DateField(null=True, blank=True)
    cdateend = models.DateField(null=True, blank=True)
    cFunction = models.CharField(max_length=20, default='')
    title = models.CharField(max_length = 200,default='')
    uploadedFile = models.FileField(upload_to=user_directory_path)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.cName