# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了

import requests
import time

url = ['https://blog.csdn.net/dagedeshu/article/details/100168495',
       'https://blog.csdn.net/dagedeshu/article/details/100064408',
       'https://blog.csdn.net/dagedeshu/article/details/100048373',
       'https://blog.csdn.net/dagedeshu/article/details/100029669',
       'https://blog.csdn.net/dagedeshu/article/details/100029660',
       'https://blog.csdn.net/dagedeshu/article/details/100029652',
       'https://blog.csdn.net/dagedeshu/article/details/100023227',
       'https://blog.csdn.net/dagedeshu/article/details/100023069',
       'https://blog.csdn.net/dagedeshu/article/details/100023033',
       'https://blog.csdn.net/dagedeshu/article/details/100020677',
       'https://blog.csdn.net/dagedeshu/article/details/100016440',
       'https://blog.csdn.net/dagedeshu/article/details/99929876',
       'https://blog.csdn.net/dagedeshu/article/details/99925518',
       'https://blog.csdn.net/dagedeshu/article/details/99883260',
       'https://blog.csdn.net/dagedeshu/article/details/99877649',
       'https://blog.csdn.net/dagedeshu/article/details/99876334',
       'https://blog.csdn.net/dagedeshu/article/details/99763604',
       'https://blog.csdn.net/dagedeshu/article/details/99700867',
       'https://blog.csdn.net/dagedeshu/article/details/99689250',
       'https://blog.csdn.net/dagedeshu/article/details/99685077',
       'https://blog.csdn.net/dagedeshu/article/details/99671496',
       'https://blog.csdn.net/dagedeshu/article/details/99657710',
       'https://blog.csdn.net/dagedeshu/article/details/99654521',
       'https://blog.csdn.net/dagedeshu/article/details/99636632',
       'https://blog.csdn.net/dagedeshu/article/details/99635814',
       'https://blog.csdn.net/dagedeshu/article/details/99539371',
       'https://blog.csdn.net/dagedeshu/article/details/99396108',
       'https://blog.csdn.net/dagedeshu/article/details/99331642',
       'https://blog.csdn.net/dagedeshu/article/details/99330840',
       'https://blog.csdn.net/dagedeshu/article/details/99289221',
       'https://blog.csdn.net/dagedeshu/article/details/99231261',
       'https://blog.csdn.net/dagedeshu/article/details/99118070',
       'https://blog.csdn.net/dagedeshu/article/details/99088352',
       'https://blog.csdn.net/dagedeshu/article/details/99064820',
       'https://blog.csdn.net/dagedeshu/article/details/98972406',
       'https://blog.csdn.net/dagedeshu/article/details/98969064',
       'https://blog.csdn.net/dagedeshu/article/details/98938093',
       'https://blog.csdn.net/dagedeshu/article/details/98885068',
       'https://blog.csdn.net/dagedeshu/article/details/98884817',
       'https://blog.csdn.net/dagedeshu/article/details/98876214',
       'https://blog.csdn.net/dagedeshu/article/details/98856773',
       'https://blog.csdn.net/dagedeshu/article/details/98487854',
       'https://blog.csdn.net/dagedeshu/article/details/98481060',
       'https://blog.csdn.net/dagedeshu/article/details/98478027',
       'https://blog.csdn.net/dagedeshu/article/details/98477243',
       'https://blog.csdn.net/dagedeshu/article/details/98354862',
       'https://blog.csdn.net/dagedeshu/article/details/98204225',
       'https://blog.csdn.net/dagedeshu/article/details/98181010',
       'https://blog.csdn.net/dagedeshu/article/details/98165335',
       'https://blog.csdn.net/dagedeshu/article/details/98056062',
       'https://blog.csdn.net/dagedeshu/article/details/97969515',
       'https://blog.csdn.net/dagedeshu/article/details/97949285',
       'https://blog.csdn.net/dagedeshu/article/details/97876435',
       'https://blog.csdn.net/dagedeshu/article/details/97875960',
       'https://blog.csdn.net/dagedeshu/article/details/97742362',
       'https://blog.csdn.net/dagedeshu/article/details/97669582',
       'https://blog.csdn.net/dagedeshu/article/details/97622323',
       'https://blog.csdn.net/dagedeshu/article/details/97613191',
       'https://blog.csdn.net/dagedeshu/article/details/97287966',
       'https://blog.csdn.net/dagedeshu/article/details/97367948',
       'https://blog.csdn.net/dagedeshu/article/details/98221250',
       'https://blog.csdn.net/dagedeshu/article/details/97285843',
       'https://blog.csdn.net/dagedeshu/article/details/97281867',
       'https://blog.csdn.net/dagedeshu/article/details/97228217',
       'https://blog.csdn.net/dagedeshu/article/details/94097569',
       'https://blog.csdn.net/dagedeshu/article/details/91947840',
       'https://blog.csdn.net/dagedeshu/article/details/91947428',
       'https://blog.csdn.net/dagedeshu/article/details/90692797',
       'https://blog.csdn.net/dagedeshu/article/details/90635793',
       'https://blog.csdn.net/dagedeshu/article/details/89945619',
       'https://blog.csdn.net/dagedeshu/article/details/89945514',
       'https://blog.csdn.net/dagedeshu/article/details/89288489',
       'https://blog.csdn.net/dagedeshu/article/details/88364765',
       'https://blog.csdn.net/dagedeshu/article/details/88364557',
       'https://blog.csdn.net/dagedeshu/article/details/87939837',
       'https://blog.csdn.net/dagedeshu/article/details/87939609',
       'https://blog.csdn.net/dagedeshu/article/details/87937533',
       'https://blog.csdn.net/dagedeshu/article/details/87937173',
       'https://blog.csdn.net/dagedeshu/article/details/87932539',
       'https://blog.csdn.net/dagedeshu/article/details/87930197',
       'https://blog.csdn.net/dagedeshu/article/details/87930095',
       'https://blog.csdn.net/dagedeshu/article/details/87910774',
       'https://blog.csdn.net/dagedeshu/article/details/87906645',
       'https://blog.csdn.net/dagedeshu/article/details/87892942',
       'https://blog.csdn.net/dagedeshu/article/details/87892793',
       'https://blog.csdn.net/dagedeshu/article/details/87891375',
       'https://blog.csdn.net/dagedeshu/article/details/87888205',
       'https://blog.csdn.net/dagedeshu/article/details/87883684',
       'https://blog.csdn.net/dagedeshu/article/details/87882109',
       'https://blog.csdn.net/dagedeshu/article/details/87881251',
       'https://blog.csdn.net/dagedeshu/article/details/87880400',
       'https://blog.csdn.net/dagedeshu/article/details/87068701',
       'https://blog.csdn.net/dagedeshu/article/details/87877809',
       'https://blog.csdn.net/dagedeshu/article/details/87873172',
       'https://blog.csdn.net/dagedeshu/article/details/87809990',
       'https://blog.csdn.net/dagedeshu/article/details/87808112',
       'https://blog.csdn.net/dagedeshu/article/details/87799280',
       'https://blog.csdn.net/dagedeshu/article/details/87798557',
       'https://blog.csdn.net/dagedeshu/article/details/87722405',
       'https://blog.csdn.net/dagedeshu/article/details/87423372'
       'https://blog.csdn.net/dagedeshu/article/details/87248942',
       'https://blog.csdn.net/dagedeshu/article/details/87423372',
       'https://blog.csdn.net/dagedeshu/article/details/87276910',
       'https://blog.csdn.net/dagedeshu/article/details/86692349',
       'https://blog.csdn.net/dagedeshu/article/details/86998108',
       'https://blog.csdn.net/dagedeshu/article/details/86774902',
       'https://blog.csdn.net/dagedeshu/article/details/86773935',
       'https://blog.csdn.net/dagedeshu/article/details/86770341',
       'https://blog.csdn.net/dagedeshu/article/details/86768475',
       'https://blog.csdn.net/dagedeshu/article/details/86768721',
       'https://blog.csdn.net/dagedeshu/article/details/86692488',
       'https://blog.csdn.net/dagedeshu/article/details/86735551',
       'https://blog.csdn.net/dagedeshu/article/details/86692879',
       'https://blog.csdn.net/dagedeshu/article/details/84108242',
       'https://blog.csdn.net/dagedeshu/article/details/86688543',
       'https://blog.csdn.net/dagedeshu/article/details/86687924',
       'https://blog.csdn.net/dagedeshu/article/details/86665136',
       'https://blog.csdn.net/dagedeshu/article/details/86663764',
       'https://blog.csdn.net/dagedeshu/article/details/86663653'
       'https://blog.csdn.net/dagedeshu/article/details/86663584',
'https://blog.csdn.net/dagedeshu/article/details/86658976',
'https://blog.csdn.net/dagedeshu/article/details/86658448',
'https://blog.csdn.net/dagedeshu/article/details/86653925',
'https://blog.csdn.net/dagedeshu/article/details/86653905',
'https://blog.csdn.net/dagedeshu/article/details/86653905',
'https://blog.csdn.net/dagedeshu/article/details/86646922',
'https://blog.csdn.net/dagedeshu/article/details/86646440',
'https://blog.csdn.net/dagedeshu/article/details/86642534',
'https://blog.csdn.net/dagedeshu/article/details/86644445',
'https://blog.csdn.net/dagedeshu/article/details/86635689',
'https://blog.csdn.net/dagedeshu/article/details/86620044',
'https://blog.csdn.net/dagedeshu/article/details/86604275',
'https://blog.csdn.net/dagedeshu/article/details/86603982',
       'https://blog.csdn.net/dagedeshu/article/details/86603926',
'https://blog.csdn.net/dagedeshu/article/details/86602515',
'https://blog.csdn.net/dagedeshu/article/details/86602360',
'https://blog.csdn.net/dagedeshu/article/details/86602001',
   'https://blog.csdn.net/dagedeshu/article/details/86588560',
'https://blog.csdn.net/dagedeshu/article/details/86569340',
'https://blog.csdn.net/dagedeshu/article/details/86583758',
'https://blog.csdn.net/dagedeshu/article/details/86568522',
   'https://blog.csdn.net/dagedeshu/article/details/86561387',
'https://blog.csdn.net/dagedeshu/article/details/86559020',
'https://blog.csdn.net/dagedeshu/article/details/86510069',
'https://blog.csdn.net/dagedeshu/article/details/86497561',
       'https://blog.csdn.net/dagedeshu/article/details/100301033',
       'https://blog.csdn.net/dagedeshu/article/details/86496685',
       'https://blog.csdn.net/dagedeshu/article/details/86481278',
       'https://blog.csdn.net/dagedeshu/article/details/86232202',
'https://blog.csdn.net/dagedeshu/article/details/86480780',
       'https://blog.csdn.net/dagedeshu/article/details/86479943',
'https://blog.csdn.net/dagedeshu/article/details/86479392',
       'https://blog.csdn.net/dagedeshu/article/details/86244092',
'https://blog.csdn.net/dagedeshu/article/details/86230487',
       'https://blog.csdn.net/dagedeshu/article/details/84574429',
'https://blog.csdn.net/dagedeshu/article/details/83385859',
       'https://blog.csdn.net/dagedeshu/article/details/83313040',
       'https://blog.csdn.net/dagedeshu/article/details/83040104',
       'https://blog.csdn.net/dagedeshu/article/details/82877617',
       'https://blog.csdn.net/dagedeshu/article/details/82720509'



       ]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

count = 0
countUrl = len(url)

# 访问次数设置
while count < 3000:
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
        time.sleep(35)

    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(60)