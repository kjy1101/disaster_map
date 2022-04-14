import time
import retrieve, classify
import pandas as pd
queries = [] # 전체 쿼리
queries_typhoon = ["태풍"] # 태풍
queries_downpour = ["폭우", "호우", "비 많", "비가", "장마"] # 호우/폭우
queries_snow = ["눈 많이", "폭설", "대설", "눈 쌓여"] # 폭설/대설
queries_gale = ["바람", "강풍", "바람 강해"] # 강풍/풍랑
queries_drought = ["가뭄", "메마름", "건조"] # 가뭄
queries_forestfire = ["산불", "화재", "건조"] # 산불
queries_earthquake = ["지진", "땅이 흔들", "진동"] # 지진
queries_coldwave = ["한파", "추위", "추워", "춥다", "추움", "얼었", "칼바람", "추운", "영하", "기온이 낮", "온도가 낮", "혹한기", "추웠"] # 한파
queries_heatwave = ["폭염", "열대야", "더위", "더워", "덥다", "더움", "더운", "고온", "이상고온", "기온이 높", "습도", "온도가 높", "혹서기", "에어컨", "더웠"] # 폭염/열대야
queries_dust = ["미세먼지", "황사", "초미세먼지", "대기오염", "뿌옇", "뿌연", "공기", "공기가 탁", "대기질"] # 미세먼지/황사

def main(interval=60):

    queries = queries_typhoon + queries_downpour + queries_snow + queries_gale + queries_drought + queries_forestfire + queries_earthquake + queries_coldwave + queries_heatwave + queries_dust

    while True:
        print("****START****")
        
        t0 = time.time()

        # 트윗 가져오기 (retrieve)
        twids, times, texts, users = retrieve.search_tweets(queries) # 추출
        twids, times, texts, users = retrieve.remove_duplicates(twids, times, texts, users) # 중복제거
        print(twids)
        print(times)
        print(texts)
        print(users)

        #df = pd.DataFrame(data, index = pd.to_datetime(times), columns = ['user_name', 'tweet', 'target', 'class', 'prob'])
        #print(data)
        t1 = time.time()

        print('retrieve: {:.2f}s'.format(t1-t0))

        if len(texts) > 0: # 분석할 트윗이 존재

            t2 = time.time()

            # 트윗 분류하기 (classify)
            tweet_classify = classify.classify_tweets(texts) # 텍스트만 가지고 트윗 분류
            print(tweet_classify)

            t3 = time.time()
            print('classify: {:.2f}s'.format(t3-t2))

            # 트윗 분석하기 (analyze)

        else: # 트윗 없음
            pass

        time.sleep(60) # 60초에 한번씩 실행


if __name__ == '__main__':
    main(interval=60)