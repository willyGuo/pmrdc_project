from ast import Try
from cgitb import enable
from curses import noecho
from email import message
import imp
from itertools import product
import re
from tkinter import N
from turtle import pos
from urllib import response
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth
from myapp.models import NewsUnit, student, requisition, clereply_db,Vote
from myapp.forms import PostForm, Requisition
import time
from . import models
from django.core.files.storage import FileSystemStorage
from django.db.models import FileField, Prefetch
import math


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
    print(students)
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
    name=request.user.username
    now = datetime.now()
    CNumber_time = cNumber_time()
    if request.user.is_authenticated:
        cName=request.user.username
    return render(request, "reply.html", locals())

def reply_submit(request):
    name=request.user.username
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
    #先判斷，request.post裡面有沒有myfile_n
    if request.POST.get('myfile_n',"no key") == "no key":
    #如果有上傳檔案就拿資料，拿完資料後比較檔案大小
        #if not request.FILES['myfile_n']:
        uploadedFile = request.FILES['myfile_n']
        title = request.FILES.get('myfile_n')
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
    else:
        unit = requisition.objects.create(cSpecial = cSpecial,cName=cName, cNumber=cNumber,cProjectname = cProjectname, cCusetername = cCusetername, \
                cProjectcode = cProjectcode, cLocation = cLocation,\
                cContent = cContent, cLastproject = cLastproject,cType=cType, cCotpye=cCotpye,\
                    cStage=cStage, cNoted=cNoted, cdatestart = cdatestart, cdateend=cdateend,cFunction=cFunction)
        unit.save()
        message = "已儲存..."
        page= "../replyshow/" + str(cNumber) + "/show"
        return redirect(page)


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

def replyshow(request, id=None, mode=None, select=None):
    name=request.user.username
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
    if mode == "will":
        unit = requisition.objects.get(cNumber=id)
        unitvotefirst = Vote.objects.all().order_by('id').select_related('cVotenumber')
        votealready = "No"
        cName = name
        cVotenumber = id
        for i in unitvotefirst:
            if unit.cName == i.cName and str(unit.cNumber) == str(i.cVotenumber):
                votealready = "Yes"
                print("我有到這裡")
                print(i.cVotenumber)
                voteconfirm = i.cVoteselect
                break
        return render(request, "replyshowwill.html", locals())
    if mode == "confirm":
        cName = name
        cVotenumber = id
        unit = requisition.objects.get(cNumber=id)
        votealready = False
        if select == "yes":
            cVoteselect = True
            unitvote = Vote.objects.create( cName= cName, cVotenumber = unit, cVoteselect = cVoteselect)
            unitvote.save()
            voteconfirm = True
            return render(request, "replyshowwill.html", locals())
        elif select == "no":
            cVoteselect = False
            unitvote = Vote.objects.create( cName= cName, cVotenumber = unit, cVoteselect = cVoteselect)
            unitvote.save()
            voteconfirm = False
            return render(request, "replyshowwill.html", locals())
    if mode =="changewill":
        print(id)
        unit = requisition.objects.get(cNumber=id)
        unitvote = Vote.objects.filter(cName = name).select_related('cVotenumber')
        unitvote.delete()
        votealready = "No"
        return render(request, "replyshowwill.html", locals())
def replyUpdate(request, id=None, mode=None):
    name=request.user.username
    if mode =="load":
        unit = requisition.objects.get(cNumber=id)
        return render(request, "replyupdate.html", locals())
    elif mode =="save":
        name=request.user.username
        unit = requisition.objects.get(cNumber=id)
        unit.cName = request.POST['cName']
        unit.cNumber = request.POST['cNumber']
        unit.cProjectname = request.POST['cProjectname']
        unit.cCusetername = request.POST['cCusetername']
        unit.cProjectcode = request.POST['cProjectcode']
        unit.cLocation = request.POST['cLocation']
        unit.cContent = request.POST['cContent']
        unit.cLastproject = request.POST['cLastproject']
        unit.cType = request.POST['cType']
        unit.cCotpye = request.POST['cCotpye']
        unit.cStage = request.POST['cStage']
        unit.cNoted = request.POST['cNoted']
        unit.cSpecial = request.POST['cSpecial']
        unit.cdatestart = request.POST['cdatestart']
        unit.cdateend = request.POST['cdateend']
        unit.cFunction = request.POST['cFunction']
        #uploadedFile = request.POST['myfile_n']
        #如果有上傳檔案就拿資料，拿完資料後比較檔案大小
        if request.POST.get('myfile_n',"no key") == "no key":
            print("我到這裡了..............")
            unit.title = request.FILES.get('myfile_n')
            unit.uploadedFile = request.FILES['myfile_n']
            if unit.uploadedFile.size < 5242880:
                unit.save()
                message = "已儲存..."
                page= "../../replyshow/" + str(unit.cNumber) + "/show"
                return redirect(page)
            else:
                unit = requisition.objects.get(cNumber=id)
                error = "檔案大小超過5mB，請壓縮!或是不選擇(原檔案上傳)" #這裡要改7/25
                return render(request, "replyupdate.html", locals())
        else:
            unit.myfile_n = ""
            unit.uploadedFile = ""
            unit.save()
            page= "../../replyshow/" + str(unit.cNumber) + "/show"
            return redirect(page)
def will(request):
    name=request.user.username
    try:
        worklist = requisition.objects.filter(cName='willy_guo').exclude(cNumber ="").filter(cStatus="In Progress").order_by('-id')

    except:
        errormessage = " (讀取錯誤!) "
    try:
        unitvote = Vote.objects.filter(cName = name).filter(cVotenumber = worklist.cNumber)
        print("ddddd")
    except:
        voteno = "這個人還沒接過案"
        print("xxxxxxxx")
    return render(request, "will.html",locals())
def willselect(request, id= None, mode=None):
    name=request.user.username
    if request.method == "POST":
        cName = name
        cVotenumber = request.POST['cNumber']
        unit = Vote.objects.create( cName= cName, cVotenumber = cVotenumber)
        unit.save()
    return render(request, "replyshow.html", locals())
def inquire(request):
    name=request.user.username
    try:
        worklist = requisition.objects.filter(cName='willy_guo').exclude(cNumber ="").order_by('-id')    
    except:
        errormessage = " (讀取錯誤!) "
    return render(request, "inquire.html",locals())
def sign(request):
    message = "系統尚未開放"
    return render(request, "index.html",locals())
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
	if 'username' in request.session:
		message=request.session['login'] + ' 您已登出!'
		del request.session['login']	#刪除Session	
	return render(request, 'login.html',locals())
def index(request):
    if request.user.is_authenticated:
        name=request.user.username
        return render(request, "index.html", locals())
    else:
        return HttpResponse("請登入")

def clereply(request):
    name=request.user.username
    clereply_dbs = clereply_db.objects.all().order_by('product')
    print(clereply_dbs)
    return render(request, 'clereply.html', locals())

def clesign(request):
    name=request.user.username
    return render(request, 'clesign.html', locals())

page1 = 1
def news(request,pageindex=None):
    global page1  #重複開啟本網頁時需保留 page1 的值
    pagesize = 8  #每頁顯示的資料筆數
    newsall = models.NewsUnit.objects.all().order_by('-id')  #讀取新聞資料表,依時間遞減排序
    datasize = len(newsall)  #新聞筆數
    totpage = math.ceil(datasize / pagesize)  #總頁數
    if pageindex==None:  #無參數
        page1 = 1
        newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
    elif pageindex=='1':  #上一頁
        start = (page1-2)*pagesize  #該頁第1筆資料
        if start >= 0:  #有前頁資料就顯示
            newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 -= 1
    elif pageindex=='2':  #下一頁
        start = page1*pagesize  #該頁第1筆資料
        if start < datasize:  #有下頁資料就顯示
            newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 += 1
    elif pageindex=='3':  #由詳細頁面返回首頁
        start = (page1-1)*pagesize  #取得原有頁面第1筆資料
        newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]

    currentpage = page1  #將目頁前頁面以區域變數傳回html
    return render(request, "news.html", locals())

def detail(request, detailid=None):
	unit = models.NewsUnit.objects.get(id=detailid)  #根據參數取出資料
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1  #點擊數加1
	unit.save()  #儲存資料
	
	return render(request, "detail.html", locals())

def replydelete(request, number):
    name=request.user.username
    #if request.method == "POST":
    print(number)
    #cnumber = request.POST[number]
    try:
        unit = requisition.objects.get(cNumber = number)
        unit.delete()
        message="已刪除"
        worklist = requisition.objects.filter(cName='willy_guo').exclude(cNumber ="").order_by('id') 
    except:
        message="讀取錯誤"
    render(request, "inquire.html",locals())
    return redirect('/inquire/')