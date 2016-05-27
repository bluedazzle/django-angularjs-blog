# coding: utf-8

from __future__ import unicode_literals

from ProxyProducer import KuaiProducer, LiuLiuProducer, XiCiProducer
from ProxyConsumer import SpiderConsumer
from CheckConsumer import CheckConsumer

import Queue
import time


def get_proxy():
    ts = time.time()
    queue = Queue.Queue()
    ip_queue = Queue.Queue()
    number_queue = Queue.Queue()
    liu = LiuLiuProducer(queue, pages=1)
    xi = XiCiProducer(queue, pages=10)

    xi.start()
    liu.start()

    for i in range(1, 16):
        spider = SpiderConsumer(q=queue, cq=ip_queue, nq=number_queue, name='spider{0}'.format(i))
        spider.daemon = True
        spider.start()

    time.sleep(1)
    for i in range(1, 10):
        check = CheckConsumer(ip_queue, name='check{0}'.format(i))
        check.start()
    ip_queue.join()
    i = 0
    while not number_queue.empty():
        i += number_queue.get()
    print i
    print('Took {}'.format(time.time() - ts))
