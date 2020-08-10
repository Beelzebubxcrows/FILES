from django.shortcuts import render
from django.views.generic.edit import CreateView
from check.models import files
from django.core.files.storage import default_storage
import os
# Create your views here.
class upload(CreateView):
    model = files
    fields='__all__'


def convert_result(request):

    return render(request,'convert_result.html')

def landing(request):
    return render(request,'landing.html')

def  clutter(request):
    return render(request,'clutter.html')

def home(request):
    return render(request,'home.html')

def result(request):
    list_files=os.listdir('check/')
    name1=''
    name2=''
    onedone=0
    for i in list_files:
        if('txt' in i):
            if(onedone==0):
                name1=i
                os.rename('check/'+i,'check/file1.txt')
                onedone=1
            elif(onedone==1):
                name2=i
                os.rename('check/'+i,'check/file2.txt')
        if('pdf' in i):
            if(onedone==0):
                name1=i
                os.rename('check/'+i,'check/file1.txt')
                onedone=1
            elif(onedone==1):
                name2=i
                os.rename('check/'+i,'check/file2.txt')
    


    f = default_storage.open('file1.txt', 'r')
    file1=f.readlines()
    f.close()

    g= default_storage.open('file2.txt','r')
    file2=g.readlines()
    g.close()

    while(file1.count('\n')>0):
        file1.remove('\n')
    
    while(file2.count('\n')>0):
        file2.remove('\n')
    t=0
    for i in file1:
        if(i[len(i)-1]=='\n'):
            file1[t]=i[:len(i)-1]

        t=t+1

    t=0

    for i in file2:
        if(i[len(i)-1]=='\n'):
            file2[t]=i[:len(i)-1]
        t=t+1


    print(file1)
    print(file2)

    copied=[]
    for i in file1:
        if(i in file2):
            copied=copied+[i]

    percent=(len(copied)/len(file1))*100

    answers={'copied_string':copied, 'percent_copied':percent}

    print(answers)

    onedone=0
    for i in list_files:
        if('txt' in i):
            if(onedone==0):
                
                os.rename('check/file1.txt','check/'+name1)
                onedone=1
            elif(onedone==1):
                name2=i
                os.rename('check/file2.txt','check/'+name2)
        if('pdf' in i):
            if(onedone==0):
                
                os.rename('check/file1.txt','check/'+name1)
                onedone=1
            elif(onedone==1):
                name2=i
                os.rename('check/file2.txt','check/'+name2)
    
    obj= files.objects.all()
    obj.delete()


    return render(request,'result.html',{'answers':answers})
