from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()

    #exclude
    QSTO = Topic.objects.exclude(topic_name='Cricket')
    #orderby-->ascending
    QSTO = Topic.objects.all().order_by('topic_name')
    #orderby length
    QSTO = Topic.objects.all().order_by(Length('topic_name'))#ascending
    QSTO = Topic.objects.all().order_by(Length('topic_name').desc())#descending
    #slicing
    QSTO = Topic.objects.all()

    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO = Webpage.objects.all()

    #orderby
    QSWO = Webpage.objects.all().order_by('topic_name')
    #startswith lookup
    QSWO = Webpage.objects.filter(name__startswith='m')
    #endswith lookup
    QSWO = Webpage.objects.filter(name__endswith='a')
    #contains
    QSWO = Webpage.objects.filter(name__contains='a')
    #in
    QSWO = Webpage.objects.filter(name__in=('virat','Saina'))
    #date
    #regex

    d = {'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_AR(request):
    QSAO = AccessRecord.objects.all()

    #orderby-->descending
    QSAO =AccessRecord.objects.all().order_by('-author')

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

    

