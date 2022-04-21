import re
# from .main import *
# windows mecab
from eunjeon import Mecab

# mac mecab
#from konlpy.tag import Mecab

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

queries_typhoon = ["태풍"] # 태풍
queries_downpour = ["폭우", "호우", "비 많", "비가", "장마"] # 호우/폭우
queries_snow = ["눈 많이", "폭설", "대설", "눈 쌓여"] # 폭설/대설
queries_forestfire = ["산불", "화재", "건조"] # 산불
queries_earthquake = ["지진", "땅이 흔들", "진동"] # 지진
queries_coldwave = ["한파", "추위", "추워", "춥다", "추움", "얼었", "칼바람", "추운", "영하", "기온이 낮", "온도가 낮", "혹한기", "추웠"] # 한파
queries_heatwave = ["폭염", "열대야", "더위", "더워", "덥다", "더움", "더운", "고온", "이상고온", "기온이 높", "습도", "온도가 높", "혹서기", "에어컨", "더웠"] # 폭염/열대야
queries_dust = ["미세먼지", "황사", "초미세먼지", "대기오염", "뿌옇", "뿌연", "공기", "공기가 탁", "대기질"] # 미세먼지/황사

region_seoul = ["서울", "서울특별시", "송파", "강서", "강남", "노원", "관악", "은평", "양천", "성북", "강동", "서초"]
region_gyeoung = ["경기", "경기도", "수원", "고양", "용인", "성남", "부천", "화성", "남양주", "안산", "안양", "평택"]
region_gang = ["강원", "강원도", "원주", "춘천", "강릉", "속초"]
region_chungbuk = ["충북", "충청북도", "청주", "충주"]
region_chungnam = ["충남", "충청남도", "천안", "아산",]
region_jeounbuk = ["전북", "전라북도", "전주", "익산"]
region_jeounam = ["전남", "전라남도", "여수", "순천",]
region_gyeoungbuk = ["경상북도", "경북", "포항","구미"]
region_gyeoungnam = ["경남", "경상남도", "창원", "김헤", "양산", "진주", "거제"]
region_busan = ["부산", "부산광역시"]
region_incheoun = ["인천", "인천광역시"]
region_daegu = ["대구", "대구광역시"]
region_ullsan = ["울산", "울산광역시"]
region_gwang = ["광주", "광주광역시"]
region_daejun = ["대전", "대전광역시"]
region_saejon = ["세종", "세특별자치시"]
region_jeju = ["제주", "제주도", "서귀포", "제주특별자치도"]

def txt2wak(txt):
    # windows mecab
    m = Mecab(dicpath='C:/mecab/mecab-ko-dic')

    # mac mecab
    #m = Mecab()

    region_tag = "None"
    disaster_tag = "None"

    for w in m.pos(txt):
        if w[0] in region_seoul:
            region_tag = "서울특별시"
            break
        elif w[0] in region_gyeoung:
            region_tag = "경기도"
            break
        elif w[0] in region_gang:
            region_tag = "강원도"
            break
        elif w[0] in region_chungbuk:
            region_tag = "충청북도"
            break
        elif w[0] in region_chungnam:
            region_tag = "충청남도"
            break
        elif w[0] in region_jeounbuk:
            region_tag = "전라북도"
            break
        elif w[0] in region_jeounam:
            region_tag = "전라남도"
            break
        elif w[0] in region_gyeoungbuk:
            region_tag = "경상북도"
            break
        elif w[0] in region_gyeoungnam:
            region_tag = "경상남도"
            break
        elif w[0] in region_busan:
            region_tag = "부산광역시"
            break
        elif w[0] in region_incheoun:
            region_tag = "인천광역시"
            break
        elif w[0] in region_daegu:
            region_tag = "대구광역시"
            break
        elif w[0] in region_ullsan:
            region_tag = "울산광역시"
            break
        elif w[0] in region_gwang:
            region_tag = "광주광역시"
            break
        elif w[0] in region_daejun:
            region_tag = "대전광역시"
            break
        elif w[0] in region_saejon:
            region_tag = "세종특별자치시"
            break
        elif w[0] in region_jeju:
            region_tag = "제주특별자치도"
            break

    for w in m.pos(txt):
        if w[0] in queries_typhoon:
            disaster_tag = "태풍"
            break
        elif w[0] in queries_downpour:
            disaster_tag = "폭우"
            break
        elif w[0] in queries_snow:
            disaster_tag = "폭설"
            break
        elif w[0] in queries_forestfire:
            disaster_tag = "산불"
            break
        elif w[0] in queries_earthquake:
            disaster_tag = "지진"
            break
        elif w[0] in queries_coldwave:
            disaster_tag = "한파"
            break
        elif w[0] in queries_heatwave:
            disaster_tag = "폭염"
            break
        elif w[0] in queries_dust:
            disaster_tag = "미세먼지"
            break

    # print(region_tag, disaster_tag)

    return disaster_tag, region_tag

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
    disasters = []
    regions = []

    for tw in tweets:
        d, r = tweet2wak(tw)
        disasters.append(d)
        regions.append(r)
        
    return disasters, regions
        

# receive list of Tweet and return list of tag of those 
def classify_tweets(twts):
    disasters, regions = tweets2tokens(twts) # 트윗->토큰 변환
    # print("disasters: ", disasters)
    # print("regions: ", regions)
    return disasters, regions

# classify_tweets(["대구 산불 뉴스 보고 양구 사는 지인 한테 괜찮냐고 톡 했는데... 집 근처라며 보내준 사진... 진짜 세상에 무슨일이야 ㅠㅠㅠㅠㅠㅠ", "창원에 지진났어요? 쿠우웅거리던데...", "어제 밤부터 시작된 제주의 바람은 2022년 첫 태풍이라고....아 기후위기 너무 온몸으로 체감 되고요 여름이 빨리 오려나 ", "눈 많이 왔어"])