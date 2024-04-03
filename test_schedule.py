import schedule
from datetime import datetime


def task():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts)


def task2():
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d %H:%M:%S")
    print(ts + '666!')


def func():
    # 清空任务
    schedule.clear()
    # 创建一个按3秒间隔执行任务
    schedule.every(3).seconds.do(task)
    # 创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(task2)
    while True:
        schedule.run_pending()


func()