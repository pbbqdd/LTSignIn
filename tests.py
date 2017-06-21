import urllib, urllib2, cookielib, sys, time,datetime

url1="deviceOS=android5.1&mobile=**********************&netWay=WIFI&deviceCode=000000000000000&isRemberPwd=true&version=android%405.3&deviceId=000000000000000&password=***********************&keyVersion=&provinceChanel=general&deviceModel=Custom+Phone+-+5.1.0+-+API+22+-+768x1280&deviceBrand=unknown&timestamp="
url2="deviceOS=android5.1&mobile=***********************&netWay=WIFI&deviceCode=000000000000000&isRemberPwd=true&version=android%405.3&deviceId=000000000000000&password=**********************&keyVersion=&provinceChanel=general&deviceModel=Custom+Phone+-+5.1.0+-+API+22+-+768x1280&deviceBrand=unknown&timestamp="


# mobile=后一串加密
# password=后一串加密
#嗅探时候ping一下m.client.10010.com，找到对应IP，设立过滤，找到相应请求即可。
#app用的平台是模拟器。
class Qiandao():
    def __init__(self):
        self.timestamp=time.strftime("%Y%m%d%H%M%S",time.localtime())
        self.cookie=cookielib.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(opener)

    def qiandao(self,url):
        req2 = urllib2.Request("http://m.client.10010.com/mobileService/login.htm",url+self.timestamp)
        urllib2.urlopen(req2)
        try:
            for item in self.cookie:
                if item.name=='a_token':
                    a=item.value
                    print a
                    req3 = urllib2.Request("http://m.client.10010.com/SigninApp/signin/querySigninActivity.htm?token="+a)
                    urllib2.urlopen(req3)
            req4 = urllib2.Request("http://m.client.10010.com/SigninApp/signin/daySign.do","btnPouplePost")
            print urllib2.urlopen(req4).read()
            req5 = urllib2.Request("http://m.client.10010.com/SigninApp/signin/goldTotal.do")
            print urllib2.urlopen(req5).read()
        except :
            print "can't login"

if __name__ == '__main__':
    user = Qiandao()
    user.qiandao(url1)
    user.qiandao(url2)