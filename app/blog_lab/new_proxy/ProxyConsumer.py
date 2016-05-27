# coding: utf-8

from __future__ import unicode_literals


from SpiderFactory import SpiderFactory


import Queue
import threading


class BaseConsumer(threading.Thread):
    def __init__(self, q, cq, nq, name='BaseCon'):
        super(BaseConsumer, self).__init__()
        self.q = q
        self.cq = cq
        self.nq = nq
        self.name = name
        self.factory = SpiderFactory()

    def run(self):
        while True:
            try:
                resource = self.q.get(block=True, timeout=3)
                spider = self.factory.create_spider(resource)
                addr_list = spider.run()
                self.nq.put(len(addr_list), block=True, timeout=3)
                for addr in addr_list:
                    self.cq.put(addr, block=True, timeout=3)
                    # print addr
                self.q.task_done()
            except Queue.Empty:
                break
            except Exception, e:
                print e
                pass
        print '{0} finish consumer works'.format(self.name)


class SpiderConsumer(BaseConsumer):
    def __init__(self, q, cq, nq, name='SpiderCon'):
        super(SpiderConsumer, self).__init__(q, cq, nq, name)
