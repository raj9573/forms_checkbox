from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    
    if request.method=='POST':
        tn=request.POST['topic_name']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('the topic is inserted successfully')
        
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST['topic']
        nm=request.POST['nm']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=nm,url=ur)[0]
        W.save()
        return HttpResponse('Data inserted through webpage is successfull')

    return render(request,'insert_webpage.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)

    return render(request,'select_topic.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    return render(request,'checkbox.html',d)