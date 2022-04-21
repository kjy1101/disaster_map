# -*- coding: utf-8 -*-
import time
#import retrieve, classify
from .retrieve import *
from .classify import *
from .models import *

queries = [] # 전체 쿼리
queries_typhoon = ["태풍"] # 태풍
queries_downpour = ["폭우", "호우", "비 많", "비가", "장마"] # 호우/폭우
queries_snow = ["눈 많이", "폭설", "대설", "눈 쌓여"] # 폭설/대설
queries_forestfire = ["산불", "화재", "건조"] # 산불
queries_earthquake = ["지진", "땅이 흔들", "진동"] # 지진
queries_coldwave = ["한파", "추위", "추워", "춥다", "추움", "얼었", "칼바람", "추운", "영하", "기온이 낮", "온도가 낮", "혹한기", "추웠"] # 한파
queries_heatwave = ["폭염", "열대야", "더위", "더워", "덥다", "더움", "더운", "고온", "이상고온", "기온이 높", "온도가 높", "혹서기", "더웠"] # 폭염/열대야
queries_dust = ["미세먼지", "황사", "초미세먼지", "대기오염", "뿌옇", "뿌연", "공기가 탁", "대기질"] # 미세먼지/황사

region = ["서울", "경기", "강원", "충북", "충남", "전북", "전라", "경북", "경남", "부산", "인천", "대구", "울산", "광주", "대전", "세종", "창원", "제주", "양구",
          "수원", "고양", "용인", "상남", "부천", "화성", "남양주", "안산", "안양", "평택", "원주", "춘천", "강릉", "속초", "청주", "충주", "천안", "아산", "포항",
          "구미", "전주", "익산", "창원", "김해", "양산", "여수", "순천", "서귀포", "양산", "진주", "거제", "서해", "남해", "동해", "일본"]

def tweet_main(interval=60):

    queries = queries_typhoon + queries_downpour + queries_snow + queries_forestfire + queries_earthquake + queries_coldwave + queries_heatwave + queries_dust

    while True:
        print("****START****")

        # t0 = time.time()

        # 트윗 가져오기 (retrieve)
        twids, times, texts, users = search_tweets(queries) # 추출
        twids, times, texts, users = remove_duplicates(twids, times, texts, users) # 중복제거
        # print(twids)
        # print(times)
        # print(texts)
        # print(users)

        #df = pd.DataFrame(data, index = pd.to_datetime(times), columns = ['user_name', 'tweet', 'target', 'class', 'prob'])
        #print(data)
        # t1 = time.time()

        # print('retrieve: {:.2f}s'.format(t1-t0))
        print("RETRIEVE END")
        
        #texts = ["양구 산불 뉴스 보고 양구 사는 지인 한테 괜찮냐고 톡 했는데... 집 근처라며 보내준 사진... 진짜 세상에 무슨일이야 ㅠㅠㅠㅠㅠㅠ", "창원에 지진났어요? 쿠우웅거리던데...", "어제 밤부터 시작된 제주의 바람은 2022년 첫 태풍이라고....아 기후위기 너무 온몸으로 체감 되고요 여름이 빨리 오려나 ", "눈 많이 왔어"]

        if len(texts) > 0: # 분석할 트윗이 존재

            # t2 = time.time()

            # 트윗 분류하기 (classify)
            # tweet_classify = classify.classify_tweets(texts) # 텍스트만 가지고 트윗 분류
            # print(tweet_classify)
            disasters, regions = classify_tweets(texts)

            # t3 = time.time()
            # print('classify: {:.2f}s'.format(t3-t2))
            print("CLASSIFY END")
            print(texts)
            print(disasters)
            print(regions)

            for twid, time, text, user, disaster, region in zip(twids, times, texts, users, disasters, regions):
                if disaster != "None":
                    tag_d = DisasterTag.objects.get(name=disaster)
                    mark = Mark.objects.get(pk=7)
                    tweet = Tweet(
                        twid=twid,
                        time=time,
                        text=text,
                        user=user,
                        disaster_tag=tag_d,
                        location=mark
                    )
                    tweet.save()
                else: # 잘못 들어온 트윗은 저장X
                    pass

        else: # 트윗 없음
            pass

        #time.sleep(1) # 60초에 한번씩 실행


if __name__ == '__main__':
    tweet_main(interval=60)