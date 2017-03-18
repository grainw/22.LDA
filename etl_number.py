#-*-coding:utf-8 -*-
import numpy as np
import pandas as pd
inputfile='news_cut.txt'

f=open(inputfile).readlines()

def load_stopword():
    f_stop = open('22.stopword.txt')
    sw = [line.strip() for line in f_stop]
    f_stop.close()
    return sw
words=[]
stop_words=load_stopword()
for i in f:
    words.extend([word for word in i.strip().lower().split() if word not in stop_words])
words=list(set(words))
print len(words)
# np 一定也有相应的用法，先实现一版之后再说。
# for i in f :
#     for j in words:
#     np.array()
# np.array(i.split())
#一定要把经典代码都写一遍。

df=pd.read_table(inputfile)
mat=[]
for  idx ,series in df.iterrows():
    arr = []
    for word in words:
        arr.append(series["content"].count(word))
    mat.append(arr)
df_norm=pd.DataFrame(mat)
print type(df_norm)
df_norm.to_excel('outputfile.xlsx')
from sklearn.decomposition import PCA
pca=PCA(n_components=100)
newData=pca.fit_transform(df_norm)
newData=pd.DataFrame(newData)
print type(newData)
newData.to_excel('out_jw.xlsx')
