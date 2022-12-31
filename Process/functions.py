import datetime
from datetime import timedelta
from time import strptime
import pandas as pd
import numpy as np

# reset index
def reset(data):
    data = data.reset_index()
    data.drop('index', axis=1, inplace=True)
    return data

# UTC 00:00 to UTC + 09:00
def to_local(data):
    data = reset(data)
    data['time'] = data['time'].str.replace('T', ' ')
    ldf=list(data['time'])
    time = pd.DataFrame(columns=['time'])
    for i in ldf:
        timestring = i[:19]
        logdate = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9)
        time.loc[i] = logdate
    time = time.reset_index()
    data.time = time.time
    data = reset(data)
    return data

# mean of weather features
def to_weather(data):
    data = data.dropna()
    data = reset(data)
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
    for i in range(0, len(data)):
        if data.loc[i, 'time'].minute > 30:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0, second=0)
            data.loc[i, 'time'] = data.loc[i, 'time'] + datetime.timedelta(hours=1)
        else:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0, second=0)
    data = data.groupby(['time'],as_index=False).mean()
    return data

# mean of api weather features
def to_api_weather(data, id):
    data = data[data['id']==id]
    data = to_local(data)
    data = data.dropna()
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
    for i in range(len(data)):
        if data.loc[i, 'time'].minute > 30:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0)
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(second=0)
            data.loc[i, 'time'] = data.loc[i, 'time'] + datetime.timedelta(hours=1)
        else:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0)
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(second=0)
    data = data.groupby(['time'],as_index=False).mean()
    return data

# mean of envs features
def to_envs(data):
    data = reset(data)
    data['time'] = data['time'].str.replace('T', ' ')
    ldf=list(data['time'])
    time = pd.DataFrame(columns=['time'])
    for i in ldf:
        timestring = i[:19]
        time.loc[i] = timestring
    time = time.reset_index()
    data.time = time.time

    data = data.dropna()
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
    for i in range(len(data)):
        if data.loc[i, 'time'].minute > 0:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0)
            data.loc[i, 'time'] = data.loc[i, 'time'] + datetime.timedelta(hours=1)
        else:
            data.loc[i, 'time'] = data.loc[i, 'time'].replace(minute=0)
    data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S')
    data = data.groupby(['time'],as_index=False).mean()
    return data

# get id of pv_gen & UTC 00:00 to UTC +09:00
def to_gen(data, id):
    data = data.rename(columns={'pv_id':'id'})
    data = data[data['id']==id]
    data = reset(data)
    data['time'] = data['time'].str.replace('T', ' ')
    ldf=list(data['time'])
    time = pd.DataFrame(columns=['time'])
    for i in ldf:
        timestring = i[:19]
        time.loc[i] = timestring
    time = time.reset_index()
    data.time = time.time
    data = reset(data)
    data = to_local(data)
    return data

# reset index & time process of historical data(gens)
def first_gens(data):
    data = reset(data)
    ldf=list(data['time'])
    time = pd.DataFrame(columns=['time'])
    for i in ldf:
        timestring = i[:19]
        time.loc[i] = timestring
    time = time.reset_index()
    data.time = time.time
    return data

# reset index & time process of historical data(weathers)
def first_weather(data, id):
    data = data[data['id']==id]
    data = reset(data)
    data['time'] = data['time'].str.replace('T', ' ')
    ldf=list(data['time'])
    time = pd.DataFrame(columns=['time'])
    for i in ldf:
        timestring = i[:19]
        time.loc[i] = timestring
    time = time.reset_index()
    data.time = time.time
    return data

# Moving Average
xbuf = []
firstRun = True
def MovAvgFilter_batch(x):
    global n, xbuf, firstRun
    if firstRun:
        n = 2
        xbuf = x * np.ones(n)
        firstRun = False
    else:
        for i in range(n-1):
            xbuf[i] = xbuf[i+1]
        xbuf[n-1] = x
    avg = np.sum(xbuf) / n
    return avg

# make year to hour
def ymdh(df):
    df['_datetime'] = pd.to_datetime(df['time'])
    df['year'] = df['_datetime'].apply(lambda x: x.year)
    df['month'] = df['_datetime'].apply(lambda x: x.month)
    df['day'] = df['_datetime'].apply(lambda x: x.day)
    df['hour'] = df['_datetime'].apply(lambda x: x.hour)
    df.drop(['_datetime'],axis=1, inplace=True)