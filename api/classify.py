import re
#import MeCab
from eunjeon import Mecab

reg1 = re.compile(r'https?://[a-zA-Z0-9_/:%#\$&\?\(\)~\.=+-]*') # url -> 삭제
reg2 = re.compile(r'(@)[a-zA-Z0-9_]*:*') # 계정 태그(@아이디) -> 삭제
reg3 = re.compile(r'(\d)([,.])(\d+)') # 숫자.숫자 -> 1.1로 변환
reg4 = re.compile(r'\d+') # 숫자 여러개 -> 1 하나로 줄임
reg5 = re.compile(r'[\r\n\t]+') # 줄바꿈, 탭 -> 공백으로 변환
reg6 = re.compile(r'[\.・…,]+') # 물음표/느낌표 제외 문장부호들 -> .으로 통일 
reg7 = re.compile(r'[?]+') # 물음표 여러개 -> 물음표 1개로 줄임
reg8 = re.compile(r'[!]+') # 느낌표 여러개 -> 느낌표 1개로 줄임
reg9 = re.compile(r'[\[{「〈【［≪《〔＜｛『]+') # 이렇게 생긴 문장부호들 -> <으로 통일
reg10 = re.compile(r'[\]}」〉】］≫》〕＞｝』]+') # 이렇게 생긴 문장부호들 -> >으로 통일
symbol = ['「','」','.','?','!']

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

queries = queries_typhoon + queries_downpour + queries_snow + queries_gale + queries_drought + queries_forestfire + queries_earthquake + queries_coldwave + queries_heatwave + queries_dust


def txt2wak(txt):
    m = Mecab(dicpath='C:/mecab/mecab-ko-dic')
    query_found = []
    for w in m.pos(txt):
        if w[0] in queries:
            query_found.append(w[0])
            # print(w[0])
    return query_found

# 트윗 텍스트에서 불필요하거나 의미없는 부분 제거 및 변환
def parge_tweet(tweet):
    t = tweet
    t = reg1.sub('', t) # url -> 삭제
    t = reg2.sub('', t) # 계정 태그(@아이디) -> 삭제
    t = reg3.sub(r'\1\3', t) # 숫자.숫자 -> 1.1로 변환
    t = reg4.sub('1', t) # 숫자 여러개 -> 1 하나로 줄임
    t = reg5.sub(' ', t) # 줄바꿈, 탭 -> 공백으로 변환
    t = reg6.sub('.',t) # 물음표/느낌표 제외 문장부호들 -> .으로 통일 
    t = reg7.sub('?', t) # 물음표 여러개 -> 물음표 1개로 줄임
    t = reg8.sub('!', t) # 느낌표 여러개 -> 느낌표 1개로 줄임
    t = reg9.sub('<',t) # 이렇게 생긴 문장부호들 -> <으로 통일
    t = reg10.sub('>',t) # 이렇게 생긴 문장부호들 -> >으로 통일
    return t

def tweet2wak(tweet):
    t = parge_tweet(tweet)
    return txt2wak(t)

# list of Tweet -> array of tokens
def tweets2tokens(tweets):
    query_found = []
    for tw in tweets:
        w = tweet2wak(tw)
        query_found += w
    print(query_found)
        

# receive list of Tweet and return list of tag of those 
def classify_tweets(twts):
    toks = tweets2tokens(twts) # 트윗->토큰 변환
    return toks



"""tweets_by_disaster = {
    "typhoon" : [],
    "downpour" : [],
    "snow" : [],
    "gale" : [],
    "drought" : [],
    "forestfire" : [],
    "earthquake" : [],
    "coldwave" : [],
    "heatwave" : [],
    "dust" : []
}

def classify_tweets(tweet_all):

    for tweet in tweet_all:
        
        if any(disaster in tweet["text"] for disaster in main.queries_typhoon):
            print("태풍 관련 트윗이다.")
            tweets_by_disaster["typhoon"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_downpour):
            print("폭우 관련 트윗이다.")
            tweets_by_disaster["downpour"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_snow):
            print("폭설 관련 트윗이다.")
            tweets_by_disaster["snow"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_gale):
            print("강풍 관련 트윗이다.")
            tweets_by_disaster["gale"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_drought):
            print("가뭄 관련 트윗이다.")
            tweets_by_disaster["drought"].append(tweet)
        
        elif any(disaster in tweet["text"] for disaster in main.queries_forestfire):
            print("산불 관련 트윗이다.")
            tweets_by_disaster["forestfire"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_earthquake):
            print("지진 관련 트윗이다.")
            tweets_by_disaster["earthquake"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_coldwave):
            print("한파 관련 트윗이다.")
            tweets_by_disaster["coldwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_heatwave):
            print("폭염 관련 트윗이다.")
            tweets_by_disaster["heatwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_dust):
            print("미세먼지 관련 트윗이다.")
            tweets_by_disaster["dust"].append(tweet)

        else:
            print("무관한 트윗이다.")

    return tweets_by_disaster
"""