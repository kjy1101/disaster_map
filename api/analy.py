from datetime import datetime, timedelta

import pandas as pd
import numpy as np

def collect_recent_tweets(times,texts,users,clss,prob,targets,limit_hours=3):
    # load and concat
    new_data=[[us,tw,ta,cl,pr] for us,tw,ta,cl,pr in zip(users,texts,targets,clss,prob)]
    df_old = io_gcs.load_recent_tweet()
    if df_old is None:
        # df = pd.DataFrame({'user_name':users,'tweet':texts,'target':targets,'class':clss,'prob':prob},index=pd.to_datetime(times))
        df = pd.DataFrame(new_data,index=pd.to_datetime(times),columns=['user_name','tweet','target','class','prob'])
        df.index.name = 'time'
        df.sort_index(inplace=True)
    else:
        # df_new = pd.DataFrame({'user_name':users,'tweet':texts,'target':targets,'class':clss,'prob':prob},index=pd.to_datetime(times))
        df_new = pd.DataFrame(new_data,index=pd.to_datetime(times),columns=['user_name','tweet','target','class','prob'])
        df_new.index.name = 'time'
        df_new.sort_index(inplace=True)
        df = pd.concat([df_old,df_new],sort=False)
    # remove old Tweet
    time_now = datetime.now()
    limit_time = (time_now-timedelta(hours=limit_hours)).strftime('%Y.%m.%d %H:%M:%S')
    df = df[df.index > limit_time]
    return df,time_now

ar = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(,index=pd.to_datetime(times),columns=['user_name','tweet','target','class','prob'])
df_ar = pd.DataFrame(ar)

print(ar)

print('\n')

print(df_ar)
