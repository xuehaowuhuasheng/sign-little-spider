import http.cookiejar
import io
import sys
import urllib.request
import base64
import random, time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 登录时需要POST的数据
# 打开文件
fr = open("user.txt")
# 读取文件的所有内容
res = fr.read()
fr.close()
# 默认以空格或者换行符分隔字符串
userlist = res.split()
# 循环列表，取出每一个值
for i in userlist:
    # 列表里的每一个值以“,”分隔字符串，“,”前面的值是账号，“,”后面的值是密码
    userid, password = i.split(",")
    encodeUserId = base64.b64encode(userid.encode())
    encodePw = base64.b64encode(password.encode())
    data = {'userId': encodeUserId,
            'pwd': encodePw,
            'name': encodeUserId
            }

    post_data = urllib.parse.urlencode(data).encode('utf-8')

    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = 'http://zckj.tjise.edu.cn/userLogin/userLogin'
    # 构造登录请求
    loginreq = urllib.request.Request(login_url, headers=headers, data=post_data)
    # 构造cookie
    cookie = http.cookiejar.CookieJar()
    # 由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(loginreq)

    encode4 = base64.b64encode(b'3')
    vistdata = {'roleId:': encode4,
                }
    post_vistdata = urllib.parse.urlencode(vistdata).encode('utf-8')
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 登录后才能访问的网页
    visturl = 'http://zckj.tjise.edu.cn/userLogin/chengeCurrentAccountRoleFlag'
    # 构造访问请求1
    vistreq = urllib.request.Request(visturl, headers=headers, data=post_vistdata)
    resp = opener.open(vistreq)

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    # 签到页面挂起时间3-6s
    #time.sleep(random.randint(3, 6))
    # 签到页面
    signurl = 'http://zckj.tjise.edu.cn/sign/signRecord'
    # 构造访问请求2
    signreq = urllib.request.Request(signurl, headers=headers, data=())
    resp1 = opener.open(signreq)
    responseString1 = resp1.read().decode('utf-8')

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    # 签到页面挂起时间3-6s
    # time.sleep(random.randint(3, 6))
    # 签到页面2
    signurl2 = 'http://zckj.tjise.edu.cn/sign/sign'
    # 构造访问请求3
    signreq2 = urllib.request.Request(signurl2, headers=headers, data=())
    resp2 = opener.open(signreq2)
    responseString2 = resp2.read().decode('utf-8')

    success = 'message":"success'
    result = success in responseString1
    if result:
        print(result,flush=1)
    else:
        print(result, ':', userid,flush=1)
    # 不同用户登录间隔10-80s
    #time.sleep(random.randint(10, 80))
