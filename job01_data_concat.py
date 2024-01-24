import pandas as pd
import glob
import datetime

data_path=glob.glob('./datasets/*')
print(data_path)

df = pd.DataFrame()
for path in data_path[:-1]:
    df_temp=pd.read_csv(path, index_col=0)
    df_temp.dropna(inplace=True)
    df=pd.concat([df, df_temp])
df_temp=pd.read_csv(data_path[-1])
df=pd.concat([df, df_temp])
print(df.head())
print(df['category'].value_counts())
df.info()
df.to_csv('./naver_news_titles_{}'.format(datetime.datetime.now().strftime('%Y%m%d')),index=False)