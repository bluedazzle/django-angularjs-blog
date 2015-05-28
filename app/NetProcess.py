import requests
import gevent
from gevent import monkey as curious_george
from gevent.pool import Pool
from requests import Session
import copy

curious_george.patch_all(thread=False, select=False)

class AsyncRequest(object):
    """ Asynchronous request.
    Accept same parameters as ``Session.request`` and some additional:
    :param session: Session which will do request
    :param callback: Callback called on response.
                     Same as passing ``hooks={'response': callback}``
    """
    def __init__(self, method, url, **kwargs):
        #: Request method
        self.method = method
        #: URL to request
        self.url = url
        #: Associated ``Session``
        self.session = kwargs.pop('session', None)
        if self.session is None:
            self.session = Session()

        callback = kwargs.pop('callback', None)
        if callback:
            kwargs['hooks'] = {'response': callback}

        #: The rest arguments for ``Session.request``
        self.kwargs = kwargs
        #: Resulting ``Response``
        self.response = None

    def send(self, **kwargs):
        """
        Prepares request based on parameter passed to constructor and optional ``kwargs```.
        Then sends request and saves response to :attr:`response`
        :returns: ``Response``
        """
        merged_kwargs = {}
        merged_kwargs.update(self.kwargs)
        merged_kwargs.update(kwargs)
        try:
            self.response =  self.session.request(self.method,
                                                self.url, **merged_kwargs)
        except Exception as e:
            self.exception = e
        return self

def send(r, pool=None, stream=False):
    if pool != None:
        return pool.spawn(r.send, stream=stream)
    return gevent.spawn(r.send, stream=stream)


class NetProcess(object):
    def __init__(self):
        self.__proxy = ''
        self.__cookies = {}
        self.__usecookies = False
        self.__headers = {}
        self.__useheaders = False
        self.__grequests = []

    def getCookies(self): return self.__cookies
    def setCookies(self, value):self.__cookies = value
    Cookies = property(getCookies, setCookies, "Property CookieList")

    def getProxy(self): return self.__proxy
    def setProxy(self, value):self.__proxy = value
    Proxy = property(getProxy, setProxy, "Property Proxy")

    def getHeaders(self): return self.__headers
    def setHeaders(self, value):self.__headers = value
    Headers = property(getHeaders, setHeaders, "Property Headers")



    def GetResFromRequest(self, method, requrl, encodemethod='utf-8', postDic={}, reqdata='', use_proxy=False, timeout=5):
        res = None
        requests.adapters.DEFAULT_RETRIES = 5
        try:
            if str(method).upper() == 'POST':
                if use_proxy:
                    scp = 'http://' + self.__proxy
                    proxy = {"http": scp, }
                    res = requests.post(requrl, data=postDic, proxies=proxy, cookies=self.__cookies,  headers=self.__headers, timeout=timeout)
                else:
                    res = requests.post(requrl, data=postDic, cookies=self.__cookies, headers=self.__headers, timeout=timeout)
            elif str(method).upper() == 'GET':
                if use_proxy:
                    scp = 'http://' + self.__proxy
                    proxy = {"http": scp, }
                    res = requests.get(requrl, proxies=proxy, cookies=self.__cookies, headers=self.__headers, timeout=timeout)
                else:
                    res = requests.get(requrl, cookies=self.__cookies, headers=self.__headers, timeout=timeout)
            self.__cookies = res.cookies
            # print res.headers
            return res.content
        except Exception, e:
            # print e.message
            # print e
            return e
        finally:
            pass


    def coroutine_request(self, method, requrl, encodemethod='utf-8', postDic={}, reqdata='', use_proxy=False, timeout=5):
        if use_proxy:
            scp = 'http://' + self.__proxy
            proxy = {"http": scp, }
            g_req = AsyncRequest(str(method).upper(), requrl, data=postDic, timeout=timeout, proxies=proxy)
        else:
            g_req = AsyncRequest(str(method).upper(), requrl, data=postDic, timeout=timeout)
        self.__grequests.append(g_req)
        return g_req


    def coroutine_response(self, size=None, stream=False, exception_handler=None, status_only=False):
        g_requests = list(self.__grequests)

        pool = Pool(size) if size else None
        jobs = [send(r, pool, stream=stream) for r in g_requests]
        gevent.joinall(jobs)

        ret = []
        if status_only:
            for request in g_requests:
                if request.response:
                    ret.append(copy.copy(True))
                else:
                    ret.append(copy.copy(False))
            return ret

        for request in g_requests:
            if request.response:
                ret.append(request.response)
            elif exception_handler:
                exception_handler(request, request.exception)



        return ret

    def OutPutCookie(self):
        res = {}
        for (itm, key) in self.__cookies.items():
            res[itm] = key
        return res

    def SetCookie(self, cookiestr):
        cookielist = eval(cookiestr)
        self.__cookies = cookielist
        self.__usecookies = True
        return True

    def SetHeaders(self, headerdic):
        self.__headers = headerdic
        self.__useheaders = True
        return True