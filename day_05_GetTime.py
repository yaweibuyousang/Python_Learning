#GetTime.py
#time库
#计算机时间的表达;提供获取系统时间并格式化输出功能;提供系统级精确计时功能，用于程序性能分析

'''
time库包括三类函数
时间获取:time() ctime() gmtime()
时间格式化:strftime() strptime()
程序计时:sleep(),perf_counter()

time()获取当前时间戳，即计算机内部时间值，浮点数
>>>time.time()
1516939876.6022282

ctime()获取当前时间并以易读方式表示，返回字符串
>>>time.ctime()
'Fri Jan 26 12:11:16 2018'

gmtime()获取当前时间，表示为计算机可处理的时间格式
>>>time.gmtime()
time.struct_time(tm_year=2018,tm_mon=1,tm_mday=26,tm_hour=4,tm_min=11,tm_sec=16
tm_wday=4,tm_yday=26,tm_isdst=0)


时间格式化
strftime(tpl,ts)tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量
>>>t=time.gmtime
>>>time.strftime("%Y-%m-%d %H:%M:%S",t)
'2018-01-26 12:55:20'

#格式化控制符
%Y  年份          0000~9999
%m  月份          01~12
%B  月份名称      January~December
%b  月份名称缩写  Jan~Dec
%d  日期          01~31
%A  星期          Monday~Sunday
%a  星期缩写      Mon~Sun
%H  小时(24h)     00~23
%h  小时(12h)     01~12
%p  上/下午       AM,PM
%M  分钟          00~59
%S  秒            00~59


>>>t=time.gmtime
>>>time.strftime("%Y-%m-%d %H:%M:%S",t)

>>>timeStr='2018-01-26 15:55:20'
>>>time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
time.struct_time(tm_year=2018, tm_mon=1, tm_mday=26, tm_hour=15, tm_min=55, tm_sec=20, tm_wday=4, tm_yday=26, tm_isdst=-1)
strptime(str,tpl)str是字符串形式的时间值，tpl是格式化模板字符串，用来定义输入效果
>>>timeStr='2018-01-26 12:55:20'
>>>time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
time.struct_time(tm_year=2018,tm_mon=1,tm_mday=26,tm_hour=4,tm_min=11,tm_sec=16
tm_wday=4,tm_yday=26,tm_isdst=0)

程序计时
测量时间：perf_counter()
产生时间：sleep()

perf_counter()返回一个CPU级别的精确时间计数值，单位为秒，由于这个计数值起点不确定，连续调用差值才有意义
>>>start=time.perf_counter()
318.66599499718114
>>>end=time.perf_counter()
341.3905185375658
>>>end - start
22.724523540384666

sleep(s)s模拟休眠时间，单位是秒，可以是浮点数
>>>def wait():
    time.sleep(3.3)
>>>wait()#程序将等待3.3秒后再退出
'''
