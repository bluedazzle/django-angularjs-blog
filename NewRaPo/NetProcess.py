import requests

class NetProcess(object):
    def __init__(self):
        self.__proxy = ''
        self.__cookies = {}
        self.__usecookies = False
        self.__headers = {}
        self.__useheaders = False

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
                    res = requests.post(requrl, data=postDic, proxies=proxy, headers=self.__headers, timeout=timeout)
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
            print e.message
            print e
            return e
        finally:
            pass

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
