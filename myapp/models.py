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
    cLastproject = models.CharField(max_length=100, default='',blank=True)
    cType = models.CharField(max_length=100, default='')
    cCotpye = models.CharField(max_length=100, default='')
    cProjecttype = models.CharField(max_length=100, default='',blank=True)
    cStage = models.CharField(max_length=100, default='')
    cNoted = models.CharField(max_length=100,default='',blank=True)
    cSchedule = models.CharField(max_length=100,default='',blank=True)
    cSpecial = models.CharField(max_length=100,default='',blank=True)
    cdatestart = models.DateField(null=True, blank=True)
    cdateend = models.DateField(null=True, blank=True)
    cFunction = models.CharField(max_length=20, default='')
    title = models.CharField(max_length = 200, default='',blank=True)
    uploadedFile = models.FileField(upload_to=user_directory_path,default='',blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    cStatus = models.CharField(max_length=20, default="In Progress")
    def __str__(self):
        return self.cNumber

class clereply_db(models.Model):
    product = models.CharField(max_length=50, default="")
    checklist = models.CharField(max_length=50, default="")
    producttype = models.CharField(max_length=50, default="")
    productscoreline = models.CharField(max_length=50, default="")



class NewsUnit(models.Model):  #新聞資料表
	catego =  models.CharField(max_length=10, null=False)  #類別關聯
	nickname = models.CharField(max_length=20, null=False)  #暱稱
	title = models.CharField(max_length=50, null=False)  #標題
	message = models.TextField(null=False)  #內容
	pubtime = models.DateTimeField(auto_now=True)  #發布時間
	enabled = models.BooleanField(default=False)  #是否顯示
	press = models.IntegerField(default=0)  #點擊次數
	def __str__(self):
		return self.title

class Vote(models.Model):  #新聞資料表
    cName =  models.CharField(max_length=10, null=False)  #誰投票
    #cVotenumber =  models.CharField(max_length=30, null=False)  #誰投票
    cVoteselect = models.BooleanField(default=False)
    cVotetime =  models.DateTimeField(auto_now = True) #投票時間
    cVotenumber = models.ForeignKey(requisition, on_delete=models.CASCADE)
    def __str__(self):
        return self.cName