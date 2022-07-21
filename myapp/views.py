from curses import noecho
from email import message
import imp
import re
from turtle import pos
from urllib import response
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from myapp.models import student, requisition
from myapp.forms import PostForm, Requisition
import time
from . import models
from django.core.files.storage import FileSystemStorage
from django.db.models import FileField

def cNumber_time():
    a = str((time.strftime("%Y%m%d%H%M%S", time.localtime())))
    return a

def sayhello(request):
    return HttpResponse("Hello Django!")

def hello2(request, username):
    return HttpResponse("Hello " + username)

def hello3(request, username):
    now = datetime.now()
    return render(request,"hello3.html",locals())

def hello4(request, username):
    now = datetime.now()
    return render(request,"hello4.html",locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())

def listone(request):
    now = datetime.now()
    try:
        unit = student.objects.get(cName="郭秉勳")
    except:
        errormessage = " (讀取錯誤!) "
    return render(request, "listone.html", locals())

def listall(request):
    now = datetime.now()
    try:
        students = student.objects.all().order_by('id')
    except:
        errormessage = " (讀取錯誤!) "
    return render(request, "listall.html", locals())

def post(request):
    if request.method == "POST":
        mess = request.POST['username']
    else:
        mess="表單資料尚未送出!"
    return render(request, "post.html", locals())

def post1(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cSex = request.POST['cSex']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']
        unit = student.objects.create(cName = cName, cSex = cSex, cBirthday = cBirthday, cEmail = cEmail,
        cPhone = cPhone, cAddr = cAddr )
        unit.save()
        return render(request, "post1.html", locals())
    else:
        message = "請輸入資料(資料不做驗證)"
    return render(request, "post1.html", locals())

def postform(request):  #新增資料，資料必須驗證
	postform = PostForm()  #建立PostForm物件
	return render(request, "postform.html", locals())

def postrequisitionform(request):
    postform = Requisition()
    return render(request, "postform.html", locals())	

def post2(request):
    postform = PostForm(request.POST)
    if request.method =="POST":
        if postform.is_valid():
            cName = request.POST['cName']
            cSex = request.POST['cSex']
            cBirthday = request.POST['cBirthday']
            cEmail = request.POST['cEmail']
            cPhone = request.POST['cPhone']
            cAddr = request.POST['cAddr']
            unit = student.objects.create(cName = cName, cSex = cSex, cBirthday = cBirthday, cEmail = cEmail,cPhone = cPhone, cAddr = cAddr )
            unit.save()
            message = "已儲存..."
            #return redirect('/post2')
        else:
            message = '姓名、性別、生日必須輸入!'
            postform = PostForm()
    return render(request, "post2.html", locals())

def indextest(request):
    postform = PostForm()  #建立PostForm物件
    return render(request, "indextest.html", locals())
def reply(request):
    now = datetime.now()
    CNumber_time = cNumber_time()
    if request.user.is_authenticated:
        name=request.user.username
    return render(request, "reply.html", locals())

def reply_submit(request):
    cName = request.POST['cName']
    cNumber = request.POST['cNumber']
    cProjectname = request.POST['cProjectname']
    cCusetername = request.POST['cCusetername']
    cProjectcode = request.POST['cProjectcode']
    cLocation = request.POST['cLocation']
    cContent = request.POST['cContent']
    cLastproject = request.POST['cLastproject']
    cType = request.POST['cType']
    cCotpye = request.POST['cCotpye']
    cStage = request.POST['cStage']
    cNoted = request.POST['cNoted']
    cSpecial = request.POST['cSpecial']
    cdatestart = request.POST['cdatestart']
    cdateend = request.POST['cdateend']
    cFunction = request.POST['cFunction']
    #upload file
    #print(request.FILES.get('myfile_n'))
    title = request.FILES.get('myfile_n')
    uploadedFile = request.FILES['myfile_n']
    if uploadedFile.size < 5242880:
        unit = requisition.objects.create(title=title, uploadedFile=uploadedFile,cSpecial = cSpecial,cName=cName, cNumber=cNumber,cProjectname = cProjectname, cCusetername = cCusetername, \
            cProjectcode = cProjectcode, cLocation = cLocation,\
            cContent = cContent, cLastproject = cLastproject,cType=cType, cCotpye=cCotpye,\
                cStage=cStage, cNoted=cNoted, cdatestart = cdatestart, cdateend=cdateend,cFunction=cFunction)
        unit.save()
        message = "已儲存..."
        page= "../replyshow/" + str(cNumber) + "/show"
        return redirect(page)
    else:
        error = "(檔案大小超過5mB，請壓縮!)"
        return render(request, "reply.html", locals())


def save_file(file):
    with open('somefile.txt','wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)

def delete(request):
    if request.method == "POST":
        id = request.POST['cId']
        try:
            unit = student.objects.get(id = id)
            unit.delete()
            message="已刪除"
        except:
            message="讀取錯誤"
    return render(request, "delete.html", locals())

def edit(request, id=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(id= id)
        unit.cName = request.GET['cName']
        unit.cSex = request.GET['cSex']
        unit.cBirthday = request.GET['cBirthday']
        unit.cEmail = request.GET['cEmail']
        unit.cPhone = request.GET['cPhone']
        unit.cAddr = request.GET['cAddr']
        unit.save()
        message= "已修改.."
    else:
        try:
            unit = student.objects.get(id=id)
            strdate = str(unit.cBirthday)
            strdate2 = strdate.replace("年","-")
            strdate2 = strdate.replace("月","-")
            strdate2 = strdate.replace("日","-")
            unit.cBirthday = strdate2
        except:
            message = "此id不存在"
    return render(request, "edit.html", locals())

def replyshow(request, id=None, mode=None):
    if mode == "show":
        unit = requisition.objects.get(cNumber=id)
        # unit.cName = request.GET['cName']
        # unit.cNumber = request.GET['cNumber']
        # unit.cProjectname = request.GET['cProjectname']
        # unit.cCusetername = request.GET['cCusetername']
        # unit.cProjectcode = request.GET['cProjectcode']
        # unit.cLocation = request.GET['cLocation']
        # unit.cContent = request.GET['cContent']
        # unit.cLastproject = request.GET['cLastproject']
        # unit.cType = request.GET['cType']
        # unit.cCotpye = request.GET['cCotpye']
        # unit.cStage = request.GET['cStage']
        # unit.cNoted = request.GET['cNoted']
        # unit.cSchedule = request.GET['cSchedule']
        # unit.cSpecial = request.GET['cSpecial']
        # message= "已修改.."
    return render(request, "replyshow.html", locals())



def edit2(request, id=None, mode=None):
    if mode =="load":
        unit = student.objects.get(id=id)
        strdate = str(unit.cBirthday)
        strdate2 = strdate.replace("年","-")
        strdate2 = strdate.replace("月","-")
        strdate2 = strdate.replace("日","-")
        unit.cBirthday = strdate2
        return render(request, "edit2.html", locals())
    elif mode =="save":
        unit = student.objects.get(id=id)
        unit.cName = request.POST['cName']
        unit.cSex = request.POST['cSex']
        unit.cBirthday = request.POST['cBirthday']
        unit.cEmail = request.POST['cEmail']
        unit.cPhone = request.POST['cPhone']
        unit.cAddr = request.POST['cAddr']
        unit.save()
        message = "已修改"
        return redirect('/index2')

def index2(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "index2.html", locals())	
        
def index3(request):
    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"])
        counter+=1
    else:
        counter =1
    response = HttpResponse("今日瀏覽次:" + str(counter))
    tomorrow = datetime.now() + timedelta(days =1)
    tomorrow = datetime.replace(tomorrow, hour=0, minute = 0, second =0)
    expires = datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie("counter", counter,expires=expires)
    return response

def vote(request):
    if not "vote" in request.session:
        request.session["vote"] = True
        msg="第一次投票"
    else:
        msg = "第二次投票"
    response = HttpResponse(msg)
    return response

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                message = '登入成功！'
                request.session["login"] = True
                return redirect('/index/')

            else:
                message = '帳號尚未啟用！'
        else:
            message = '登入失敗！'
    return render(request, "login.html", locals())

def logout(request):
    del request.session['login']
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                message = '登入成功！'
                return redirect('/index/')

            else:
                message = '帳號尚未啟用！'
        else:
            message = '登入失敗！'
    return render(request, "login.html", locals())
	
def logout(request):
	if 'username' in request.session:
		message=request.session['username'] + ' 您已登出!'
		del request.session['username']	#刪除Session	
	return render(request, 'login.html',locals())
def index(request):
    if request.user.is_authenticated:
        name=request.user.username
    return render(request, "index.html", locals())