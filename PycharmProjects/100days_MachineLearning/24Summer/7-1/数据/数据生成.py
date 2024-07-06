# -*- coding: utf-8 -*-
# @Author: bd
# @Date:   2024-02-29 17:28:15
# @Last Modified by:   bd
# @Last Modified time: 2024-03-01 10:33:35

import numpy as np
import pandas as pd
import pickle,os


def core():
    from joblib import Parallel, delayed
    url='E:/数据库/拆分数据/'
    col=['日期', '股票代码', '股票名称', '开盘价', '最高价', '最低价', '收盘价','涨跌幅','流通股']
    def fuc(filename):
        url='E:/数据库/拆分数据/'
        ticker=filename[:6]
        # print(ticker,end='-')
        try:
            data=pd.read_csv(open(f'{url}{ticker}.csv'))
            data=data[data['成交量(万股)']!=0]
            data=data[data['成交量(万股)'].isna()==False]
        except:return [{}]
        if len(data)<30:return [{}]
        data['涨跌幅']=(data['收盘价']-data['收盘价'].shift(1))/data['收盘价'].shift(1)*100
        data['涨跌幅']=data['涨跌幅'].round(2)
        data['流通股']=data['流通股(亿)'].round(2)
        return data[col].iloc[-2:].to_dict('records')
    info=Parallel(n_jobs=12)(delayed(fuc)(x)for x in os.listdir(url))
    # info=[fuc('000025.csv')]
    # raise
    # info=[fuc(os.listdir(url)[1173])]
    # raise
    info=[y for x in info for y in x if y!={}]
    info=pd.DataFrame(info)
    da1=sorted(list(set(info['日期'])))
    da1,da2=da1[-2],da1[-1]
    info=info[(info['日期']==da1)|(info['日期']==da2)]
    info=info.to_dict('split')
    data=[info['columns']]+info['data']
    # print(data)
    # raise
    # info[col].to_csv(open(f'选出.csv','w'),index=False,line_terminator="\n")
    with open("个股数据.pickle", "wb") as f:
        pickle.dump(data, f)

def get_tickerdata():
    with open("数据/个股数据.pickle", "rb") as f:
        data = pickle.load(f)
    return data

def core1():
    with open("东财概念对应表.pickle", "rb") as f:
        data = pickle.load(f)
    print(data.keys())
    a={}
    for x in ['汽车芯片','工业母机','网络安全','增强现实','智能电网','氢能源','中药','煤化工','量子通信']:
        a[x]=data[x]
    with open("指数成分股.pickle", "wb") as f:
        pickle.dump(a, f)


def get_index_ticker_dict():
    with open("数据/指数成分股.pickle", "rb") as f:
        data = pickle.load(f)
    return data


def get_tickerlist():
    url='数据/拆分数据/'
    return os.listdir(url)

def function(fnn):
    url='数据/拆分数据/'
    ticker=fnn[:6]
    # print(ticker,end='-')
    try:
        data=pd.read_csv(open(f'{url}{ticker}.csv'))
        data=data[data['成交量(万股)']!=0]
        data=data[data['成交量(万股)'].isna()==False]
    except:return pd.DataFrame()
    data['涨跌幅']=(data['收盘价']-data['收盘价'].shift(1))/data['收盘价'].shift(1)*100
    data['涨跌幅']=data['涨跌幅'].round(2)
    data['流通股']=data['流通股(亿)'].round(2)
    return data

if __name__ == '__main__':
    # print(get_tickerdata())
    core1()
