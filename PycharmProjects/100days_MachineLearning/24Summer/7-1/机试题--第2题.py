# -*- coding: utf-8 -*-
# @Author: bd
# @Date:   2024-02-29 16:47:18
# @Last Modified by:   bd
# @Last Modified time: 2024-03-01 10:21:47
from  数据.数据生成 import *
import numpy as np
import pandas as pd
'''
题目：两日行业主题指数编制：编制指数，根据提供的数据，计算并输出所有指数两日的每日指数涨幅。
指数编制旨在创建一个能够反映特定市场或资产类别的表现的工具，编制行业主题指数则是为了聚焦讲述特定行业的故事。

相关定义与公式如下：

股票A流通市值=股票A流通股本*股票A当日收盘价

指数成分股，是指参与指数编制的股票名单，在名单内的股票参与此指数的编制，不在名单内的股票不参与此指数的编制。
示例：{指数A：[股票代码A，股票代码B，股票代码C.....]，
 指数B：[股票代码B，股票代码E，股票代码F.....]，....}

指数涨幅为指数内包含的成分股的流通市值加权平均和，即
指数涨幅=（股票A当日涨跌幅*股票A当日流通市值+股票B当日涨跌幅*股票B当日流通市值......）/（股票A当日流通市值+股票B当日流通市值.....）

数据提取方式：
股票数据：get_tickerdata()
示例：
[['日期', '股票代码', '股票名称', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '流通股'],
 ['2024-02-28', 1, '平安银行', 10.51, 10.7, 10.4, 10.49, -0.1, 194.06], 
 ['2024-02-29', 1, '平安银行', 10.42, 10.59, 10.41, 10.59, 0.95, 194.06], 
 ['2024-02-28', 2, '万  科Ａ', 10.06, 10.16, 9.93, 9.93, -1.29, 97.17], 
 ['2024-02-29', 2, '万  科Ａ', 9.85, 10.04, 9.84, 10.04, 1.11, 97.17], 
 ..........
 ]
指数成分股数据：get_index_ticker_dict()
注：如遇到疑问可咨询面试官。
代码运行：点击上方任务栏---》工具---》编译，或直接按快捷键Ctrl+B
'''

# print(get_tickerdata())
# print(get_index_ticker_dict())

ticker_data = get_tickerdata()
index_ticker_dict = get_index_ticker_dict()

columns = ticker_data[0]
data = ticker_data[1:]
df = pd.DataFrame(data,columns = columns)

df['流通市值'] = df['收盘价'] * df['流通股']

def calculate_index_return(df,index_ticker_dict):
    dates = df['日期'].unique()
    res = []
    for data in dates:
        daily_data = df[df['日期'] == data]
        for index_name,ticker in index_ticker_dict.items():
            index_data = daily_data[daily_data['股票代码'].isin(ticker)]
            if not index_data.empty:
                total_market_cap = index_data['流通市值'].sum()
                weighted_return = (index_data['涨跌幅'] * index_data['流通市值']).sum() / total_market_cap
                res.append([data,index_name,weighted_return])
    return pd.DataFrame(res,columns = ['日期','指数名称','涨幅'])

index_returns = calculate_index_return(df,index_ticker_dict)
print(index_returns)


