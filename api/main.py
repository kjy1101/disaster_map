# -*- coding: utf-8 -*-
import time
from .retrieve import *
from .classify import *
from .models import *
from apscheduler.schedulers.background import BackgroundScheduler

queries = [] # 전체 쿼리
queries_typhoon = ["태풍"] # 태풍
queries_downpour = ["폭우", "호우", "비 많", "비가", "장마"] # 호우/폭우
queries_snow = ["눈 많이", "폭설", "대설", "눈 쌓여"] # 폭설/대설
queries_forestfire = ["산불", "화재", "건조"] # 산불
queries_earthquake = ["지진", "땅이 흔들", "진동"] # 지진
queries_coldwave = ["한파", "추위", "추워", "춥다", "추움", "얼었", "칼바람", "추운", "영하", "기온이 낮", "온도가 낮", "혹한기", "추웠"] # 한파
queries_heatwave = ["폭염", "열대야", "더위", "더워", "덥다", "더움", "더운", "고온", "이상고온", "기온이 높", "온도가 높", "혹서기", "더웠"] # 폭염/열대야
queries_dust = ["미세먼지", "황사", "초미세먼지", "대기오염", "뿌옇", "뿌연", "공기가 탁", "대기질"] # 미세먼지/황사

queries = queries_typhoon + queries_downpour + queries_snow + queries_forestfire + queries_earthquake + queries_coldwave + queries_heatwave + queries_dust

def job():
    print("****START****")

    # 트윗 가져오기 (retrieve)
    twids, times, texts, users = search_tweets(queries) # 추출
    twids, times, texts, users = remove_duplicates(twids, times, texts, users) # 중복제거
        
    if len(texts) > 0: # 분석할 트윗이 존재

        # 트윗 분류하기 (classify)
        disasters, regions = classify_tweets(texts)
        print(texts)
        print(disasters)
        print(regions)

        for twid, time, text, user, disaster, region in zip(twids, times, texts, users, disasters, regions):
            if disaster != "None" and region != "None":
                tag_d = DisasterTag.objects.get(name=disaster)
                mark = Mark.objects.get(region_name=region)
                tweet = Tweet(
                    twid=twid,
                    time=time,
                    text=text,
                    user=user,
                    disaster_tag=tag_d,
                    location=mark
                )
                tweet.save()
            else:  # 잘못 들어온 트윗은 저장X
                pass

    else: # 트윗 없음
        pass
    
    print("************************")

def cron_tweet():
    print("cron start")
    sched = BackgroundScheduler()
    sched.add_job(job, 'interval', seconds=60, id='cron_tweet')
    sched.start()