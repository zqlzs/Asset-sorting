import re

ip = []
ym = []
url = []
urlp = []
z = []

with open('资产列表.txt','r') as ff:

    zc = ff.read().splitlines()
    comip = re.compile(r'^((2((5[0-5])|([0-4]\d)))|([0-1]?\d{1,2}))(\.((2((5[0-5])|([0-4]\d)))|([0-1]?\d{1,2}))){3}$')
    comym = re.compile(r'^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$')
    comurl = re.compile(r'^(?=^.{3,255}$)(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\d+)*(\/\w+\.\w+)*$')
    comurlp = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    for i in zc:
        # print(i)
        if comip.match(i):
            # print('ip资产为：', i)
            if i not in ip:
                ip.append(i)
            # dip(i)
            continue
        elif comym.match(i):
            # print('域名资产为：', i)
            if i not in ym:
                ym.append(i)
            # dym(i)
            continue
        elif comurl.match(i):
            # print('url资产为：', i)
            if 'http' not in i:
                a = re.findall(r'(.*):', i)
                if comip.match(a[0]):
                    if a[0] not in ip:
                        ip.append(a[0])
                else:
                    if a[0] not in ym:
                        ym.append(a[0])
                # z.append(a[0])
                continue
            a = re.findall(r'https?:\/\/(.*)?', i)
            if '/' in a[0]:
                # print(i)
                if i not in urlp:
                    urlp.append(i)
                a = re.findall(r'(.*)?\/', i)
                # print(a[0])
                if ':' in a[0]:
                    d = re.findall(r'https?:\/\/(.*)?', a[0])
                    # print(d)
                    if ':' in d[0]:
                        b = re.findall(r'(.*):', d[0])
                        # print('域名资产为：', b)
                        if comip.match(b[0]):
                            if b[0] not in ip:
                                ip.append(b[0])
                        else:
                            if b[0] not in ym:
                                ym.append(b[0])
                    else:
                        if comip.match(d[0]):
                            if d[0] not in ip:
                                ip.append(d[0])
                        else:
                            if d[0] not in ym:
                                ym.append(d[0])
                else:
                    # print('域名资产为：', a[0])
                    if comip.match(a[0]):
                        if a[0] not in ip:
                            ip.append(a[0])
                    else:
                        if a[0] not in ym:
                            # print(a[0])
                            ym.append(a[0])
                continue
            else:
                if i not in url:
                    url.append(i)
            if ':' in a[0]:
                b = re.findall(r'(.*):', a[0])
                # print('域名资产为：', b[0])
                if comip.match(b[0]):
                    if b[0] not in ip:
                        ip.append(b[0])
                else:
                    if b[0] not in ym:
                        ym.append(b[0])
            else:
                # print('域名资产为：', a[0])
                if comip.match(a[0]):
                    if a[0] not in ip:
                        ip.append(a[0])
                else:
                    if a[0] not in ym:
                        ym.append(a[0])
            # durl(i)
            continue
        elif comurlp.match(i):
            # print('url带参数资产为：', i)
            # print(i)
            if i not in urlp:
                urlp.append(i)
            c = re.findall(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+$,\w]+@)?[A-Za-z0-9.-]+(:[0-9]+)?|(?:ww‌​w.|[-;:&=\+$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w_]*)?\??(?:[-\+=&;%@.\w_]*)#?‌​(?:[\w]*))?)', i)
            # print('url资产为：', c[0][0])
            if c[0][0] not in url:
                url.append(c[0][0])
            d = re.findall(r'https?:\/\/(.*)?', c[0][0])
            # print(d[0])
            if ':' in d[0]:
                e = re.findall(r'(.*):', d[0])
                # print(e[0])
                # print('ip资产为：', e[0])
                if comip.match(e[0]):
                    if e[0] not in ip:
                        ip.append(e[0])
                else:
                    # print('ip资产为：', d[0])
                    if e[0] not in ym:
                        ym.append(e[0])
                continue
            else:
                if comip.match(d[0]):
                    if d[0] not in ip:
                        ip.append(d[0])
                else:
                    # print('ip资产为：', d[0])
                    if d[0] not in ym:
                        ym.append(d[0])
            # durlp(i)
            continue
        else:
            # print("脏数据为：", i)
            if i not in z:
                z.append(i)
            # dz(i)

# print('ip有：', ip, '数据保存在ip.txt')
f = open('./result/ip.txt', 'w', encoding='utf-8')
for i in ip:
    f.write(i+'\n')
f.close()

# print('域名有：', ym, '数据保存在ym.txt')
f = open('./result/域名.txt', 'w', encoding='utf-8')
for i in ym:
    f.write(i+'\n')
f.close()

# print('url有：', url, '数据保存在url.txt')
f = open('./result/url.txt', 'w', encoding='utf-8')
for i in url:
    f.write(i+'\n')
f.close()

# print('url带参数有：', urlp, '数据保存在urlp.txt')
f = open('./result/带参数url.txt', 'w', encoding='utf-8')
for i in urlp:
    f.write(i+'\n')
f.close()

# print('脏数据有：', z, '数据保存在z.txt')
f = open('./result/脏数据.txt', 'w', encoding='utf-8')
for i in z:
    f.write(i+'\n')
f.close()

print("资产分拣已完成！")
print("ip保存在：/result/ip.txt中~")
print("域名保存在：/result/域名.txt中~")
print("url保存在：/result/url.txt中~")
print("带参数url保存在：/result/带参数url.txt中~")
print("脏数据保存在：/result/脏数据.txt中~")