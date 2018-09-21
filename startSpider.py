#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sched
import os
import time

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 被周期性调度触发的函数
def func():
    os.system("scrapy crawl evolutionLand")


def perform(inc):
    schedule.enter(inc, 0, perform, (inc,))
    func()  # 需要周期执行的函数


def mymain():
    schedule.enter(0, 0, perform, (60,))


if __name__ == "__main__":
    mymain()
    schedule.run()  # 开始运行，直到计划时间队列变成空为止
