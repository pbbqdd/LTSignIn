import urllib.request as urllib2
# from urllib import parse
import http.cookiejar
import sys, time,datetime,fileinput,os
import json
#python3环境
url=""#fiddler 抓取登录请求 exp：isRemberPwd=true&deviceId=000000000000000&password=**********&netWay=WIFI&mobile=*******************&timestamp=20181017230801&appId=1406a14ec25d9b783bc0fd29eacd072acfdae2811573d8d00d001205217142b4&keyVersion=1&deviceBrand=unknown&areaCode=940&version=android%405.93&deviceModel=Custom%20Phone%20-%205.1.0%20-%20API%2022%20-%20768x1280&deviceOS=android5.1&deviceCode=000000000000000
# token =""#token 在cookie中a_token下，可以下载android的抓包精灵在其中抓包获得。
class Qiandao():


    def __init__(self):
        self.timestamp=time.strftime("%Y%m%d%H%M%S",time.localtime())
        self.cookie=http.cookiejar.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(opener)

    def qiandao(self,url):
        req2 = urllib2.Request("http://m.client.10010.com/mobileService/login.htm",url.encode('utf-8')+self.timestamp.encode('utf-8'))
        urllib2.urlopen(req2)
        # file = os.open("cookies",1)
        # file.write(json.encoder(self.cookie))
        # file.flush()
        # file.close()

            # print(urllib2.urlopen(req2).read())
        try:
            for item in self.cookie:
                if item.name=='a_token':
                    a=item.value
                    print(a)
        except :
            print("cant get cookeis")
        req3 = urllib2.Request("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token="+a)
        urllib2.urlopen(req3)
        # print(urllib2.urlopen(req3).read())
        req4 = urllib2.Request("https://act.10010.com/SigninApp/signin/daySign.do","btnPouplePost".encode('utf-8'))
        # print(urllib2.urlopen(req4).read())
        req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/goldTotal.do")
        print (urllib2.urlopen(req5).read())


if __name__ == '__main__':
    user = Qiandao()
    user.qiandao(url)