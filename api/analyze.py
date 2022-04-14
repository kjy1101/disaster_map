import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

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


disaster = {}

typhoon_array = []
downpour_array = []
snow_array = []
gale_array = []
drought_array = []
forestfire_array = []
earthquake_array = []
coldwave_array = []
heatwave_array = []
dust_array = []

def make_dataframe(data):
    for d in data:
        if d in queries_typhoon:
            typhoon_array.append(d)
        elif d in queries_downpour:
            downpour_array.append(d)
        elif d in queries_snow:
            snow_array.append(d)
        elif d in queries_gale:
            gale_array.append(d)
        elif d in queries_drought:
            drought_array.append(d)
        elif d in queries_forestfire:
            forestfire_array.append(d)
        elif d in queries_earthquake:
            earthquake_array.append(d)
        elif d in queries_coldwave:
            coldwave_array.append(d)
        elif d in queries_heatwave:
            heatwave_array.append(d)
        elif d in queries_dust:
            dust_array.append(d)
        else:
            pass
    
    disaster = dict(typhoon = np.array(typhoon_array), 
                    downpour = np.array(downpour_array), 
                    snow = np.array(snow_array), 
                    gale = np.array(gale_array), 
                    drought = np.array(drought_array), 
                    forestfire = np.array(forestfire_array), 
                    earthquake = np.array(earthquake_array), 
                    coldwave = np.array(coldwave_array), 
                    heatwave = np.array(heatwave_array), 
                    dust = np.array(dust_array), 
                )

    # print(disaster)
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in disaster.items() ]))
    # print(df)
    print("태풍 관련 단어 빈도수: ", sum(df['typhoon'].value_counts()))
    print("호우 관련 단어 빈도수: ", sum(df['downpour'].value_counts()))
    print("폭설 관련 단어 빈도수: ", sum(df['snow'].value_counts()))
    print("강풍 관련 단어 빈도수: ", sum(df['gale'].value_counts()))
    print("가뭄 관련 단어 빈도수: ", sum(df['drought'].value_counts()))
    print("산불 관련 단어 빈도수: ", sum(df['forestfire'].value_counts()))
    print("지진 관련 단어 빈도수: ", sum(df['earthquake'].value_counts()))
    print("한파 관련 단어 빈도수: ", sum(df['coldwave'].value_counts()))
    print("폭염 관련 단어 빈도수: ", sum(df['heatwave'].value_counts()))
    print("미세먼지 관련 단어 빈도수: ", sum(df['dust'].value_counts()))

    np.random.seed(0)
    #print(np.random.randn(100,10))

    all_freq = {}
    typhoon_freq = []
    downpour_freq = []
    snow_freq = []
    gale_freq = []
    drought_freq = []
    forestfire_freq = []
    earthquake_freq = []
    coldwave_freq = []
    heatwave_freq = []
    dust_freq = []

    # 이전 빈도수 기록
    typhoon_freq = [1,2,3,4]
    downpour_freq = [0,3,5,7]
    snow_freq = [3,7,4,2]
    gale_freq = [8,4,0,2]
    drought_freq = [3,6,9,2]
    forestfire_freq = [2,5,7,9]
    earthquake_freq = [3,7,9,1]
    coldwave_freq = [3,0,8,1]
    heatwave_freq = [2,8,5,0]
    dust_freq = [2,5,7,3]

    # 이번에 불러온 트윗에서의 빈도수 추가
    typhoon_freq.append(sum(df['typhoon'].value_counts()))
    downpour_freq.append(sum(df['downpour'].value_counts()))
    snow_freq.append(sum(df['snow'].value_counts()))
    gale_freq.append(sum(df['gale'].value_counts()))
    drought_freq.append(sum(df['drought'].value_counts()))
    forestfire_freq.append(sum(df['forestfire'].value_counts()))
    earthquake_freq.append(sum(df['earthquake'].value_counts()))
    coldwave_freq.append(sum(df['coldwave'].value_counts()))
    heatwave_freq.append(sum(df['heatwave'].value_counts()))
    dust_freq.append(sum(df['dust'].value_counts()))

    all_freq["typhoon"] = typhoon_freq
    all_freq["downpour"] = downpour_freq
    all_freq["snow"] = snow_freq
    all_freq["gale"] = gale_freq
    all_freq["drought"] = drought_freq
    all_freq["forestfire"] = forestfire_freq
    all_freq["earthquake"] = earthquake_freq
    all_freq["coldwave"] = coldwave_freq
    all_freq["heatwave"] = heatwave_freq
    all_freq["dust"] = dust_freq


    df1 = pd.DataFrame(all_freq,
                   index=pd.date_range('1/1/2018', periods=5),
                   columns=['typhoon', 'downpour', 'snow', 'gale', 'drought', 'forestfire', 'earthquake', 'coldwave', 'heatwave', 'dust'])

    print(df1.tail())
    df1.plot()
    plt.title("disaster word frequency")
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.show()
    

make_dataframe(['추웠', '덥다', '공기', '비가', '바람', '태풍', '장마', '장마', '바람', '비가', '습도', '추워', '화재', '폭염', '추위', '추운', '춥다', '바람', '비가', '덥다', '바람', '건조', '춥다', '추위', '추운', '추위', '추워', '바람', '바람', '바람'])