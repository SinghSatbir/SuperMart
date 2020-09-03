# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:19:14 2019

@author: This-PC
"""

import pandas as pd
import numpy as np
import os

outfile=""
tables=[]
f=open('order.txt')
for line in f:
    tables.append(line)
f.close()
for name in tables:
    name=name[:-1]
    d=pd.read_csv('data/'+name+'.csv')
    outfile=outfile+'insert into '+name+' values\n'
    if name=='storage_area'or name=='shift' or name=='packed_food' or name=='clothes' or name=='personal_care':
        for i in range(d.shape[0]):
         #   print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
               # print(d.iloc[i,j])
                outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='department':
        for i in range(d.shape[0]):
          #  print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                    outfile=outfile+str(d.iloc[i,j])+','
                elif j==2:
                    outfile=outfile
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='employee':
        for i in range(d.shape[0]):
          #  print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==d.shape[1]-1 or j==d.shape[1]-5 or j==d.shape[1]-2:
                    outfile=outfile+str(d.iloc[i,j])+','
                elif j==0:
                    temp=d.iloc[i,j].split('-')
                    outfile=outfile+temp[0]+temp[1]+temp[2]+','
                elif j==d.shape[1]-3:
                    outfile=outfile+'to_date('+'\''+d.iloc[i,j]+'\''+', \'MM/DD/YYYY\')'+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
        
        outfile=outfile+'update department set mgrssn=175133189 where dno=1;\n'
        outfile=outfile+'update department set mgrssn=600298120 where dno=2;\n'
        outfile=outfile+'update department set mgrssn=234615106 where dno=3;\n'
        outfile=outfile+'update department set mgrssn=434481316 where dno=4;\n'
        outfile=outfile+'update department set mgrssn=481550169 where dno=5;\n'
        outfile=outfile+'update department set mgrssn=116851994 where dno=6;\n'
    elif name=='members':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='supplier':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==d.shape[1]-2:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='items':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==3:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
                else:
                    outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='product':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==2:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='packed_food_description':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j>=2 and j!=3:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='clothes_description':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==d.shape[1]-1:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='personal_care_description':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j>=2 and j!=4 and j!=3:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='shift_assigns':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                    outfile=outfile+str(d.iloc[i,j])+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='attendance':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                    outfile=outfile+str(d.iloc[i,j])+','
                elif j==d.shape[1]-1 :
                    outfile=outfile+'\''+str(d.iloc[i,j]).lower()+'\','
                elif j==d.shape[1]-2 :
                    outfile=outfile+'to_date('+'\''+d.iloc[i,j]+'\''+', \'MM/DD/YYYY\')'+','
                else:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='supply_record':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                     outfile=outfile+'\''+d.iloc[i,j]+'\','
                elif j==2:
                    outfile=outfile+'to_date('+'\''+d.iloc[i,j]+'\''+', \'MM/DD/YYYY\')'+','
                else:
                    outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='discount':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j>1:
                     outfile=outfile+'to_date('+'\''+d.iloc[i,j]+'\''+', \'MM/DD/YYYY\')'+','
                else:
                   outfile=outfile+'\''+d.iloc[i,j]+'\','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='discount_products':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                     outfile=outfile+'\''+d.iloc[i,j]+'\','
                else:
                   outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='discount_products':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                     outfile=outfile+'\''+d.iloc[i,j]+'\','
                else:
                   outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='bill':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if j==0:
                     outfile=outfile+str(d.iloc[i,j])+','
                elif j==1:
                    outfile=outfile+'to_date('+'\''+d.iloc[i,j]+'\''+', \'MM/DD/YYYY\')'+','
                elif j==2:
                    outfile=outfile+'time '+'\''+d.iloc[i,j]+'\','
                elif j==4:
                    outfile=outfile+'\''+d.iloc[i,j]+'\','
                elif j==5:
                    temp=d.iloc[i,j].split('-')
                    outfile=outfile+temp[0]+temp[1]+temp[2]+','
                else:
                   outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='bill_details':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
    elif name=='complain':
        for i in range(d.shape[0]):
           # print(d.iloc[i,:])
            outfile=outfile+'('
            for j in range(d.shape[1]):
                if (j>=1 and j<=4) or j==6:
                    if d.iloc[i,j]!='\'NULL\'':
                        outfile=outfile+'\''+(d.iloc[i,j])+'\','
                    else:
                        outfile=outfile+str(d.iloc[i,j][1:-1])+','
                elif j==5:
                    temp=d.iloc[i,j].split('-')
                    outfile=outfile+temp[0]+temp[1]+temp[2]+','
                else:
                   outfile=outfile+str(d.iloc[i,j])+','
            outfile=outfile[:-1]+'),\n'
        outfile=outfile[:-2]+';\n'
with open('insertion_script.txt', "w", encoding="utf-8") as f:
    f.write(outfile)
        
    