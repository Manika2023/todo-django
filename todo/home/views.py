from django.shortcuts import render,HttpResponse
from home.models import Task
# Create your views here.
def home(request):
     context={
               'success':False,
               'miss':""
          }
     miss=""
     if request.POST.get('title')=='':
            return render(request,"index.html",{'error':True, 'miss':"SORRY! you have missed your title,please try again! "})
     miss=""
     if request.POST.get('desc')=='':
            return render(request,"index.html",{'error':True, 'miss':"SORRY! you have missed your desc,please try again! "})       
     if request.method=="POST":
          title=request.POST.get('title')
          desc=request.POST.get('desc')
          ins=Task(taskTitle=title,taskDese=desc)
          ins.save()
          context={
               'success':True
          }
     return render(request,'index.html',context)

def tasks(request):
     allTasks=Task.objects.all()
     context={
           'tasks':allTasks
     }
     return render(request,'tasks.html',context)

