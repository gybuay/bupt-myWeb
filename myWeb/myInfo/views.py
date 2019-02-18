from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from .models import *
import os
import urllib.parse
from django.utils.encoding import escape_uri_path
from django.contrib import messages
# Create your views here.

#receive HttpRequest
def index(request):
    # return HttpResponse
    #return HttpResponse('<h1>ggggg<h1>')
    #context = {'title':'django','list':range(10)}
    #return render(request,'myInfo/index.html',context=context)
    #到settings.py中templates的目录里面找

    # list = ExamInfo.objects.all()
    # context = {'examlist':list}
    #return render(request, 'myInfo/filelist.html')
    path = os.path.abspath('.')
    path = os.path.join(path, 'static/upload/')
    path = path.replace('/', '\\')
    pathDir = os.listdir(path)
    allFile = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (path, allDir))
        allFile.append(child)  # .decode('gbk')是解决中文显示乱码问题
    context = {'path': pathDir, 'download': 'download/?d_id='}
    return render(request, 'myInfo/filelist.html', context)

def exam(request,id):#id从\d传过来
    #context = {'id':id}
    if id=='1':#注意是str，不是int
        return render(request, 'myInfo/exam1.html')
    elif id=='2':
        return render(request, 'myInfo/exam2.html')
    elif id=='3':
        return render(request, 'myInfo/exam3.html')
    else:
        return render(request, 'myInfo/exam4.html')

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理

        context = readFileList() #读取显示目录

        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            messages.error(request, "请选择需要上传的文件")#弹窗提醒
            return render(request, 'myInfo/filelist.html', context)
        # path = os.path.join("../static/upload/",myFile.name)
        # path = path.replace(r'\\',r'/')
        path = os.path.abspath('.')
        path = os.path.join(path,'static/upload/')
        path = os.path.join(path,myFile.name)
        path = path.replace('/', '\\')

        #abs_path = os.path.join(r'D:\develop\myWeb\static\upload',myFile.name)
        destination = open(path,'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        #return HttpResponse(os.path.join("upload/",myFile.name))
        messages.success(request, '上传成功')#弹窗提醒

        context = readFileList()#若上传成功目录会更改，再次读取

        return render(request, 'myInfo/filelist.html', context)

def filelist(request):
    path = os.path.abspath('.')
    path = os.path.join(path, 'static/upload/')
    path = path.replace('/', '\\')
    pathDir = os.listdir(path)
    allFile = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (path, allDir))
        allFile.append(child)  # .decode('gbk')是解决中文显示乱码问题
    context = {'path':pathDir, 'download':'download/?d_id='}
    return render(request, 'myInfo/filelist.html', context)

def download(request):
    the_file_name = request.GET.get('d_id')# 显示在弹出对话框中的默认的下载文件名
    the_file_name = urllib.parse.unquote(the_file_name)#url解析中文文件名转码
    path = os.path.abspath('.')
    path = os.path.join(path, 'static/upload/')
    path = path.replace('/', '\\')

    filename = os.path.join(path,the_file_name) # 要下载的文件路径

    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'\
        .format(escape_uri_path(the_file_name))#escape_uri_path解决中文名字文件问题

    #ss = str(type(the_file_name.encode('utf-8')))

    return response
    #return HttpResponse(filename+ "          " +the_file_name + ss)


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
    f.close()


def readFileList():
    path = os.path.abspath('.')
    path = os.path.join(path, 'static/upload/')
    path = path.replace('/', '\\')
    pathDir = os.listdir(path)
    allFile = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (path, allDir))
        allFile.append(child)  # .decode('gbk')是解决中文显示乱码问题
    context = {'path': pathDir, 'download': 'download/?d_id='}
    return context


