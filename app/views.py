from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from app.models import*
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is submiited')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    return render (request,'insert_topic.html')

    
def insert_web(request):
    topic=Topic.objects.all()
    d={'topic':topic }
    if request.method=='POST':
       
        topic=request.POST['topic']
        n=request.POST['n']
        u=request.POST['u']

        TO=Topic.objects.get(topic_name=topic)
        TO.save()
        
        wo=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        wo.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_web.html',d)


def insert_access(request):
    webpage=Webpage.objects.all()
    d={'webpage:webpage'}

    if request.method=='POST':
        
        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']
        wo=Webpage.objects.get(name=n)
        ao=AccessRecord.objects.get_or_create(name=wo,date=d,authour=a)[0]
        ao.save()
        return HttpResponse('data inserted to accessrecord')
    return render(request,'insert_access.html')
























        
       


