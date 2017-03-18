import numpy as np
f=open('../data/22.news.dat').readlines()

def load_stopword():
    f_stop = open('22.stopword.txt')
    sw = [line.strip() for line in f_stop]
    f_stop.close()
    return sw
words=[]
stop_words=load_stopword()
for i in f:
    words=words+[word for word in i.strip().lower().split() if word not in stop_words]
words=set(words)
for i in f :
    for j in words:


    np.array()
np.array(i.split())

