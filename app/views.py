from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO = Webpage.objects.all()
    d = {'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_AR(request):
    QSAO = AccessRecord.objects.all()
    d = {'QSAO':QSAO}
    return render(request,'display_AR.html',d)

def insert_topic(request):
    tn = input('Enter topic name: ')
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()

    QSTO = Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn = input('Enter topic name: ')
    n = input('Enter name: ')
    url = input('Enter URL: ')

    TO = Topic.objects.get(topic_name = tn)

    WO = Webpage.objects.get_or_create(topic_name = TO, name = n, url = url)[0]
    WO.save()

    QSWO = Webpage.objects.all()
    d = {'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def insert_AC(request):
    d = input('Enter date: ')
    a = input('Enter author: ')
    e = input('Enter email: ')
    pk = int(input('Enter primary key: '))


    WO = Webpage.objects.get(pk=pk)

    AO = AccessRecord.objects.get_or_create(name= WO, date = d, author = a, email = e)[0]
    AO.save()

    QSAO = AccessRecord.objects.all()
    d = {'QSAO':QSAO}
    return render(request,'display_AR.html',d)

    

