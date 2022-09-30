"""web_devp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from requests import delete
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello2/<str:username>/', views.hello2),
    path('index/', views.index),
    path('',views.login),
    path('logout/',views.logout),
    path('hello3/<str:username>', views.hello3),
    path('hello4/<str:username>', views.hello4),
    path('listone/',views.listone),
    path('listall', views.listall),
    path('post1/', views.post1),
    path('post2/', views.post2),
    path('post/',views.post),
    path('index2/', views.index2),
    path('delete/', views.delete),
    path('indextest/',views.indextest),
    path('reply/',views.reply,name='my-view'),
    path('testurl/',views.reply_submit),
    path('will/',views.will),
    path('sign/',views.sign),
    path('inquire/',views.inquire),
    path('edit/<int:id>/', views.edit),
    path('replyshow/<str:id>/<str:mode>',views.replyshow),
    path('replyshow/<str:id>/<str:mode>/<str:select>',views.replyshow),
    #path('replyshow/<str:id>/<str:mode>',views.willselect),
    path('replyupdate/<str:id>/<str:mode>',views.replyUpdate),
    path('edit/<int:id>/<str:mode>', views.edit),
    path('edit2/<int:id>/<str:mode>', views.edit2),
    #path('postform/', postform),
    #path('postreq/', postrequisitionform),
    path('index3/',views.index3),
    path('vote/', views.vote),
    path('login/', views.login),
    path('logout/', views.logout),
    #CLE系統
    path('clereply/', views.clereply),
    path('clesign/', views.clesign),
    path('news/<str:pageindex>/', views.news),
    path('news/', views.news),
    path('detail/<int:detailid>/', views.detail),
    path('replydelete/<str:number>/', views.replydelete),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)