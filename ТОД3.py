import json
import csv
import pandas as pd
import numpy as np
import pickle
import os
import requests
from bs4 import BeautifulSoup
def usernames(x):
    if x in contributors['username'].unique():
        print(contributors.loc[contributors['username']==x])
    else:
        print('ValueError')
contributors=pd.read_json('contributors_sample.json')
print('1.1 Выведена информация о первых 3 пользователях: ','\n',contributors.head(3),'\n')
print('1.2 Уникальные почтовые домены: ','\n',pd.unique(contributors['mail']),'\n')
print('1.3 Введите username : ')
usernames(input())
print('1.3 Задание выполнено!','\n')
print('1.4 Количество женщин: ',contributors['sex'].value_counts()[0])
print('1.4 Количество мужчин: ',contributors['sex'].value_counts()[1],'\n')
df=pd.concat([contributors['id'],contributors['username'],contributors['sex']],axis=1)
print('1.5 ДатаФрейм содержащий столбцы: id, username и sex','\n',df)
recipes=pd.read_csv('recipes_sample.csv',parse_dates=['submitted'])
recipes1=recipes.merge(contributors,on=['id'])
print('1.6 Таблицы объединены! Количество человек, информация о которых отсутствует: ',len(contributors.id)-len(recipes.id),'\n')
D={}
with open('contributors_sample.json') as f:
    data=json.load(f)
    for i in range(len(data)):
        for j in range(len(data[i]['jobs'])):
            if data[i]['jobs'][j] in D.keys():
                D[data[i]['jobs'][j]].append(data[i]['username'])
            else:
                D[data[i]['jobs'][j]]=[]
                D[data[i]['jobs'][j]].append(data[i]['username'])
print('2.1 Задание выполнено !')
with open('job_people.pickle','wb') as file:
    pickle.dump(D,file)
with open('job_people.json', 'w') as fp:
    json.dump(D,fp,indent=' ')
print('2.2 Размер файла job_people.pickle :',os.path.getsize('job_people.pickle'))
print('2.2 Размер файла job_people.json :',os.path.getsize('job_people.json'))
with open('job_people.pickle','rb') as file:
    p=pickle.load(file)
print('2.3 Демонстрация считывания файла job_people.pickle:','\n')
print(p)
with open('steps_sample.xml') as file:
    dt=BeautifulSoup(file,'xml')
D1={}
D2={}
A=dt.find_all('id')
A1=dt.find_all('steps')
A2=[]
for i in range(len(A)):
    A[i]=int(A[i].get_text())
    if 'step has_minutes="1"' in str(A1[i]):
        A2.append(A[i])
    A1[i]=A1[i].get_text().split('\n')
    A1[i].pop(0)
    A1[i].pop(-1)
    D1[A[i]]=A1[i]
    key=len(A1[i])
    if pd.isnull(recipes.n_steps.loc[recipes.id==A[i]]).values ==True:
        recipes.loc[recipes.id==A[i],['n_steps']]=len(A1[i])
    if key in D2:
        D2[key].append(int(A[i]))
    else:
        D2[key]=[]
        D2[key].append(int(A[i]))
with open('steps_sample.json', 'w') as fp1:
    json.dump(D1,fp1)
print('3.1 Задание выполнено! ')
print('3.2 Задание выполнено! ')
print('3.3 Задание выполнено! ')
print('3.4 Задание выполнено! ')
print('3.5 Количество пропусков в таблице: ',recipes.n_steps.isnull().sum ())
recipes.to_csv('recipes_sample_with_filled_nsteps.csv')
print('3.5 Задание выполнено! ')
