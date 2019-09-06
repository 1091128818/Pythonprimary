#导包
import numpy as np
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
from datetime import datetime
import calendar
import matplotlib.pyplot as plt
import seaborn as sn

#读入数据
bikedata=pd.read_csv("train.csv");

#数据提取
def collect_and_process_data():
    bikedata['date']=bikedata.datetime.apply(lambda x:x.split()[0])
    bikedata['year'] = bikedata.date.apply(lambda x: x.split("/")[0])
    bikedata['hour']=bikedata.datetime.apply(lambda x:x.split()[1].split(':')[00])
    bikedata['weekday']=bikedata.date.apply(lambda dateString:calendar.day_name[datetime.strptime(dateString,'%Y/%m/%d').weekday()])
    bikedata['month']=bikedata.date.apply(lambda dateString:calendar.month_name[datetime.strptime(dateString,'%Y/%m/%d').month])


     #数据转化
    bikedata['season'] = bikedata.season.map({1:'Spring',2:'Summer',3:'Autumn',4:'Winter'})
    varlist=['hour','weekday','month','year','season','holiday','workingday']
    for x in varlist:
        bikedata['hour'] = bikedata['hour'].astype('int')
        bikedata[x]=bikedata[x].astype('category')
    bikedata.drop('datetime',axis=1,inplace=True)

    # 处理数据
    #bikedata['season']
    fig, axes = plt.subplots(nrows=2, ncols=2)#plt包里的包 绘制子图 如果里面没有，默认绘制一个
    fig.set_size_inches(12,12)
    sn.boxplot(data=bikedata,y="count",orient="v",ax=axes[0][0])
    sn.boxplot(data=bikedata,y="count",x="season",orient="v",ax=axes[0][1])
    sn.boxplot(data=bikedata,y="count",x="hour",orient="v",ax=axes[1][0])
    sn.boxplot(data=bikedata,y="count",x="workingday",orient="v",ax=axes[1][1])
    #绘图
    axes[0][0].set(ylabel='骑行人数',title="骑行人数")
    axes[0][1].set(ylabel='骑行人数',xlabel='季节',title="不同季节骑行人数")
    axes[1][0].set(xlabel='时间',ylabel='骑行人数',title="一天不同时间骑行人数")
    axes[1][1].set(xlabel='工作日',ylabel='骑行人数',title="工作日骑行人数")
    plt.savefig("Abnormal_value_analysis.png")
    plt.show()

    #剔除数据
    bikedata1 = bikedata[np.abs(bikedata["count"] - bikedata["count"].mean()) <=(3 * bikedata["count"].std())]
    #三倍标准差剔除异常值 abs绝对值 mean平均
    bikedata1.to_csv('processed_data.csv')
    return bikedata1

#后面的绘图分析
def Data_Analysis_and_Visualization_month(bikedata1):
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(12,20)
    sortOrder = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    monthAggregated = pd.DataFrame(bikedata1.groupby("month")["count"].mean()).reset_index()
    # print(monthAggregated)
    monthSorted = monthAggregated.sort_values(by="count",ascending=False)
    # print(monthSorted)
    sn.barplot(data=monthSorted,x="month",y="count",order=sortOrder)
    ax1.set(xlabel='月份',ylabel='平均骑行人数',title="不同月份骑行人数")
    plt.savefig('result1.png')
    plt.show()

def Data_Analysis_and_Visualization_week(bikedata1):
    fig2, ax2 = plt.subplots()
    fig2.set_size_inches(12,20)
    hueOrder = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    hourAggregated = pd.DataFrame(bikedata1.groupby(["hour","weekday"])["count"].mean()).reset_index()
    sn.pointplot(x=hourAggregated["hour"],y=hourAggregated["count"],hue=hourAggregated["weekday"],hue_order=hueOrder,data=hourAggregated)
    ax2.set(xlabel='时间',ylabel='骑行人数',title='一周内不同时间的骑行人数')
    plt.savefig('result2.png')
    plt.show()

def Data_Analysis_and_Visualization_season1(bikedata1):
    fig3, ax3 = plt.subplots()
    fig3.set_size_inches(12,20)
    seasonOrder = ['Spring','Summer','Autumn','Winter']
    seasonAggregated = pd.DataFrame(bikedata1.groupby("season")["count"].mean()).reset_index()
    seasonSorted = seasonAggregated.sort_values(by="count", ascending=False)
    # print(monthSorted)
    sn.barplot(data=seasonSorted, x="season", y="count", order=seasonOrder)
    ax3.set(xlabel='时间',ylabel='骑行人数',title='一季度内不同时间的骑行人数')
    plt.savefig('result3.png')
    plt.show()

#不同用户在不同时间内的骑行人数    数字小时数
def Data_Analysis_and_Visualization_vip(bikedata1):
    fig4, ax4 = plt.subplots()
    fig4.set_size_inches(12, 20)
    hour_Transform = pd.melt(bikedata1[['hour', 'casual', 'registered']], id_vars=['hour'],
                             value_vars=['casual', 'registered'])
    hour_Aggregated3 = pd.DataFrame(hour_Transform.groupby(['hour', 'variable'])['value'].mean()).reset_index()
    sn.pointplot(data=hour_Aggregated3, x='hour', y='value', hue='variable', hue_order=['casual', 'registered'])
    ax4.set(xlabel='时间', ylabel='骑行人数', title='不同用户在不同时间的骑行人数')
    plt.savefig('result4.png')
    plt.show()

def Data_Analysis_and_Visualization_season2(bikedata1):
    fig5, ax5 = plt.subplots()
    fig5.set_size_inches(12,20)
    hueOrder = ['Spring','Summer','Autumn','Winter']
    hourAggregated = pd.DataFrame(bikedata1.groupby(["hour","season"])["count"].mean()).reset_index()

    sn.pointplot(x=hourAggregated["hour"],y=hourAggregated["count"],hue=hourAggregated["season"],hue_order=hueOrder,data=hourAggregated)
    # sn.pointplot(x=hourAggregated["hour"],y=hourAggregated["count"],hue=hourAggregated["weekday"],hue_order=hueOrder,data=hourAggregated)
    ax5.set(xlabel='时间',ylabel='骑行人数',title='不同季节的骑行人数')
    plt.savefig('result5.png')
    plt.show()

def Data_Analysis_and_Visualization_year(bikedata1):
    fig6, ax6 = plt.subplots()
    fig6.set_size_inches(12, 20)
    # 租车辆按月份、年份统计
    sortOrder = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"]
    month_Aggregated = pd.DataFrame(bikedata1.groupby(['year', 'month'])['count'].mean()).reset_index()
    sn.barplot(data=month_Aggregated, x="month", y="count", hue='year',order=sortOrder, ax=ax6)
    ax6.set(xlabel='月份', ylabel='年份', title="不同年份和月份的对比")
    plt.savefig('result6.png')
    plt.show()

def Data_Analysis_and_Visualization_season_year(bikedata1):
    fig7, ax7 = plt.subplots()
    fig7.set_size_inches(12,20)
    seasonOrder = ['Spring','Summer','Autumn','Winter']
    seasonAggregated = pd.DataFrame(bikedata1.groupby(["season","year"])["count"].mean()).reset_index()
    # print(monthAggregated)
    seasonSorted = seasonAggregated.sort_values(by="count", ascending=False)
    # print(monthSorted)
    sn.barplot(data=seasonSorted, x="season", y="count",hue='year', order=seasonOrder)
    ax7.set(xlabel='时间',ylabel='骑行人数',title='一季度内不同年的骑行人数')
    plt.savefig('result7.png')
    plt.show()


#不同用户在不同时间内的骑行人数    数字小时数
def Data_Analysis_and_Visualization_vip_week(bikedata1):
    fig8, ax8 = plt.subplots()
    fig8.set_size_inches(12, 20)
    w_cOrder = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    hour_Transform = pd.melt(bikedata1[['weekday', 'casual', 'registered']], id_vars=['weekday'],
                             value_vars=['casual', 'registered'])
    hour_Aggregated3 = pd.DataFrame(hour_Transform.groupby(['weekday', 'variable'])['value'].mean()).reset_index()
    sn.pointplot(data=hour_Aggregated3, x='weekday', y='value', hue='variable', hue_order=['casual', 'registered'],order=w_cOrder)
    ax8.set(xlabel='天数', ylabel='骑行人数', title='不同用户在不同天的骑行人数')
    plt.savefig('result8.png')
    plt.show()

#主函数
def main():
     bikedata1 = collect_and_process_data()
     Data_Analysis_and_Visualization_month(bikedata1)
     Data_Analysis_and_Visualization_week(bikedata1)
     Data_Analysis_and_Visualization_season1(bikedata1)
     Data_Analysis_and_Visualization_vip(bikedata1)
     Data_Analysis_and_Visualization_season2(bikedata1)
     Data_Analysis_and_Visualization_year(bikedata1)
     Data_Analysis_and_Visualization_season_year(bikedata1)
     Data_Analysis_and_Visualization_vip_week(bikedata1)
#主程序
if __name__ == '__main__':
    main()
