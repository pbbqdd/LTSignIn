import urllib.request as urllib2
# from urllib import parse
import http.cookiejar
import sys, time,datetime
#python3环境
token =""#token 在cookie中a_token下，可以下载android的抓包精灵在其中抓包获得。
class Qiandao():
    def __init__(self):
        self.timestamp=time.strftime("%Y%m%d%H%M%S",time.localtime())
        self.cookie=http.cookiejar.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(opener)

    def qiandao(self,token):
        # req2 = urllib2.Request("http://m.client.10010.com.ipv6.tcdnv3.com/mobileService/login.htm",url+self.timestamp)
        # urllib2.urlopen(req2)
        # print(urllib2.urlopen(req2).read())
        try:
        #     # for item in self.cookie:
        #     #     if item.name=='a_token':
        #     #         a=item.value
        #     #         print(a)
            req3 = urllib2.Request("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token="+token)
            urllib2.urlopen(req3)
            # print(urllib2.urlopen(req3).read())
            req4 = urllib2.Request("https://act.10010.com/SigninApp/signin/daySign.do","btnPouplePost".encode('utf-8'))
            print(urllib2.urlopen(req4).read())
            req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/goldTotal.do")
            print (urllib2.urlopen(req5).read())
        except :
            print("can't login")

if __name__ == '__main__':
    user = Qiandao()
    user.qiandao(token)