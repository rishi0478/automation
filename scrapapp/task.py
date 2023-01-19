
from celery import shared_task
from scrapapp.models import *
import requests
from bs4 import BeautifulSoup as bs
from django.db.models import Q

@shared_task
def Automation():
    countt = 0
    
    final =[]

    final_source , final_target = [] , []
    # source_url="https://diggitymarketing.com/custom-seo-case-study/"
    # target_url="https://thesearchinitiative.com/"

    source_url_temp = URL_NOOPENER.objects.values("source_url")
    target_url_temp = URL_NOOPENER.objects.values("target_url")
    sourceurl = list(source_url_temp)
    targeturl = list(target_url_temp)



    for i in sourceurl:
        final_source.append(i["source_url"])
    for j in targeturl:
        final_target.append(j["target_url"])

    source_url = final_source
    target_url = final_target
    tag = []


    for _ in source_url:


        try:

            if URL_NOOPENER.objects.get(Q(source_url=source_url[countt]) | Q(target_url=target_url[countt])):
                obj = URL_NOOPENER.objects.get(Q(source_url=source_url[countt]) | Q(target_url=target_url[countt]))
                response = requests.get(source_url[countt])
                soup = bs(response.content,'html.parser')
                links = soup.find_all('a',rel=True)
                for link in links:
                    a = link['href']
                    if a==target_url[countt]:
                        
                        final.append(link) #link
            
                        for i in final:
                            det=i.get('href')
                            no=i.get('rel')
                            tag.append(det)

                data=URL_NOOPENER(id =obj.id, source_url=source_url[countt],target_url=target_url[countt],links=list(set(tag)),noopener=no)    
                data.save()
        except Exception as e:

            response = requests.get(source_url[countt])
            soup = bs(response.content,'html.parser')
            links = soup.find_all('a',rel=True)
            for link in links:
                a = link['href']
                if a==target_url[countt]:
                    
                    final.append(link) #link
        
                    for i in final:
                        det=i.get('href')
                        no=i.get('rel')
                        tag.append(det)

            data=URL_NOOPENER.objects.create(source_url=source_url[countt],target_url=target_url[countt],links=list(set(tag)),noopener=no)    
            data.save()

        #celeryurl
        try:
            if URL.objects.get(Q(source_url=source_url[countt]) | Q(target_url=target_url[countt])):
                objj = URL.objects.get(Q(source_url=source_url[countt]) | Q(target_url=target_url[countt]))
                
                responses = requests.get(source_url[countt])
                mysoup = bs(responses.content,'html.parser')
                # first
                linkss = mysoup.find_all('a',rel=False)
                my_final = []
                for linkl in linkss:
                    a = linkl['href']
                    if a==target_url[countt]:
                        my_final.append(a)
                dataa=URL(id = objj.id,source_url=source_url[countt],target_url=target_url[countt],links=my_final)     
                dataa.save()
        except Exception as e:
            responses = requests.get(source_url[countt])
            mysoup = bs(responses.content,'html.parser')
            # first
            linkss = mysoup.find_all('a',rel=False)
            my_final = []
            for linkl in linkss:
                a = linkl['href']
                if a==target_url[countt]:
                    my_final.append(a)
            dataa=URL.objects.create(source_url=source_url[countt],target_url=target_url[countt],links=my_final)     
            dataa.save()


        countt +=1 
    return "success"

 #celery 
#command1=celery -A scrapproject worker -l info -P gevent
# command2=celery -A scrapproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler   