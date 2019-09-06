#导包操作
#from wxpy import *
#import matplotlib.pylot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
import re
import jieba
import numpy as np
from scipy.misc import imread
from wordcloud import WordCloud
import itchat

itchat.auto_login()

# bot =Bot()
# all_friends = bot.friends()
# print(all_friends)
# Official_Accounts = bot.mps()
# current_group_chat = bot.groups()
# #friend = bot.friends()search('asd')[0]
# print(friend)
# friend.send("全民制作人大家好")
