import json
import datetime

## Json配置文件读取
with open("config/time0.json", encoding = "utf-8") as cfg:
    tcfg = json.load(cfg)
with open("config/cur0.json", encoding = "utf-8") as cfg:
    ccfg = json.load(cfg)

## 计算当前为第几教学周

def get_toordinal(origin_day, sun):
    """返回当周周一的公历序数；若sun为true，则返回周日（返回的均为比当前日期早、或当天）"""
    weekday_num = origin_day.weekday()
    the_day = origin_day - datetime.timedelta(days=weekday_num)
    t_num = datetime.date.toordinal(the_day)
    if sun:
        if weekday_num == 6:
            t_num += 6
        else:
            t_num -= 1
    return t_num

start_day = datetime.datetime.strptime(tcfg['start'],'%Y-%m-%d').date()
start_toordinal = get_toordinal(start_day, tcfg['sun-first'])

now_toordinal = get_toordinal(datetime.date.today(), tcfg['sun-first'])

week_num = int((now_toordinal - start_toordinal)/7 + 1) #教学周值

## 确定本周课程



## 创建表格输出
