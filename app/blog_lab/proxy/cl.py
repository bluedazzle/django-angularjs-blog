from app.NetProcess import NetProcess
import simplejson
import time


def doit():
    token = 'vf3kDL6bIx1lYjPeT+HuXorgtRZSdNBU'
    ip_list = []
    net = NetProcess()
    data = {'private_token': token}
    res = net.GetResFromRequest('POST', 'http://www.rapospectre.com/lab/get_proxy/', postDic=data)
    json_data = simplejson.loads(res)
    ip_body = json_data['body']['proxy_list']
    for ip in ip_body:
        new_ip = ip['ip']
        ip_list.append(new_ip)
    net.Headers = {'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; MI 2S MIUI/4.11.7)',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': '68.64.164.93'}
    for i in ip_list:
        net.Proxy = i
        res = net.GetResFromRequest('GET', 'http://68.64.164.93/u/?id=zjqqq', use_proxy=True, encodemethod='gb2312')
        # print res
        res = net.GetResFromRequest('GET', 'http://68.64.164.93/index.asp?id=zjqqq', use_proxy=True, encodemethod='gb2312')
        # print res



for j in range(1, 100):
    doit()
    print 'num %i' % j
    time.sleep(3)
# doit()
