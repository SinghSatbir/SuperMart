# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:30:25 2019

@author: This-PC
"""
import datetime
import pandas as pd
import numpy as np
df=pd.read_csv('data/bill_details - Copy.csv')
it=pd.read_csv('data/items.csv')
sr=pd.read_csv('data/supply_record.csv')
for i in range(it.shape[0]):
    q=sr[sr['itemcode']==it.iloc[i,0]]
    z=np.sum(q['qty'].values)
    if(it.iloc[i,0]==3529641701435):
        print(z,q.shape)
for i in range(it.shape[0]):
    q=df[df['itemcode']==it.iloc[i,0]]
    z=np.sum(q['qty'].values)
    if(it.iloc[i,0]==3529641701435):
        print(z,q.shape)
for i in range(it.shape[0]):
    q=sr[sr['itemcode']==it.iloc[i,0]]
    if(q.shape[0] != 0):
        z=np.sum(q['qty'].values)
        q=df[df['itemcode']==it.iloc[i,0]]
        z=int(0.98*(z)/q.shape[0])
        df.loc[df['itemcode']==it.iloc[i,0],['qty']]=z

df.to_csv('data/bill_details.csv',index=False)
#    
#g={}
#x=1
#supp=sr['licenseno'].drop_duplicates(keep='first',inplace=False)
#supp=supp.values
#for i in range(supp.shape[0]):
#    g[supp[i]]=x
#    x=x+1
#d=sr.copy()
#d['licenseno']=d['licenseno'].map(lambda x : g[x])
#d.drop(['date'],axis=1,inplace=True)    
#d.drop_duplicates(subset=['licenseno','itemcode'],keep='last',inplace=True)
#for i in range(it.shape[0]):
#    q=d[d['itemcode']==it.iloc[i,0]]
#    print(q.shape)
