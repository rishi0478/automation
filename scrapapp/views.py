from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
import requests
from .task import Automation
from bs4 import BeautifulSoup as bs
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def func(request):
    final=[]
    tag=[]
    my_final = []
    if request.method=='POST':
        source_url=request.POST['surl']
        target_url=request.POST['turl']

        try:

            if URL_NOOPENER.objects.get(Q(source_url=source_url) | Q(target_url=target_url)):
                obj = URL_NOOPENER.objects.get(Q(source_url=source_url) | Q(target_url=target_url))
                print(obj.id)
                print("rishiiiiiiii")
                response = requests.get(source_url)
                soup = bs(response.content,'html.parser')
                #second
                links = soup.find_all('a',rel=True)
                for link in links:
                    a = link['href']
                    if a==target_url:
                        
                        final.append(link) #link
            
                        for i in final:
                            print(i,'-----')
                            det=i.get('href')
                            no=i.get('rel')
                            print(no,"RRRR------nnnn")
                            print(det,'====link')
                            tag.append(det)

                data=URL_NOOPENER(id = obj.id,source_url=source_url,target_url=target_url,links=list(set(tag)),noopener=no)    
                data.save()
        except Exception as e:
            print("rishi======mehra")
            response = requests.get(source_url)
            soup = bs(response.content,'html.parser')
            #second
            links = soup.find_all('a',rel=True)
            for link in links:
                a = link['href']
                if a==target_url:
                    
                    final.append(link) #link
        
                    for i in final:
                        print(i,'-----')
                        det=i.get('href')
                        no=i.get('rel')
                        print(no,"RRRR------nnnn")
                        print(det,'====link')
                        tag.append(det)

            data=URL_NOOPENER.objects.create(source_url=source_url,target_url=target_url,links=list(set(tag)),noopener=no)    
            data.save()

        #URL
        try:

            if URL.objects.get(Q(source_url=source_url) | Q(target_url=target_url)):
                objj = URL.objects.get(Q(source_url=source_url) | Q(target_url=target_url))
                responses = requests.get(source_url)
                print(responses,'response')
                mysoup = bs(responses.content,'html.parser')
                # first
                linkss = mysoup.find_all('a',rel=False)
                for linkl in linkss:
                    a = linkl['href']
                    if a==target_url:
                        # final.append(a)
                        my_final.append(a)
                dataa=URL(id = objj.id,source_url=source_url,target_url=target_url,links=my_final)     
                dataa.save()
        except Exception as e:

            responses = requests.get(source_url)
            print(responses,'response')
            mysoup = bs(responses.content,'html.parser')
            # first
            linkss = mysoup.find_all('a',rel=False)
            for linkl in linkss:
                a = linkl['href']
                if a==target_url:
                    # final.append(a)
                    my_final.append(a)
            dataa=URL.objects.create(source_url=source_url,target_url=target_url,links=my_final)     
            dataa.save()

        return render(request,'scrap_data.html',{'final':final,"my_final":my_final})
    elif request.method == "GET":
        return render(request,"scrap_data.html")


def Table_NoOpener(request):
    datas=URL_NOOPENER.objects.all()
    page= request.GET.get('page', 1)
    paginator=Paginator(datas, 100)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data= paginator.page(paginator.num_pages)
    return render(request,'noopener_table.html',{'page_obj':data})

def Table(request):
    datas=URL.objects.all()
    page= request.GET.get('page', 1)
    paginator=Paginator(datas, 100)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data= paginator.page(paginator.num_pages)
    return render(request,'table.html',{'page_obj':data})

def Delete_table(request):
    data=URL_NOOPENER.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

def Delete_table2(request):
    data=URL.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))      