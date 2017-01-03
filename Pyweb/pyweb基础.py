#python 3.x中urllib库和urilib2库合并成了urllib库。。
#其中urllib2.urlopen()变成了urllib.request.urlopen()
#   urllib2.Request()变成了urllib.request.Request()    
import urllib    
import cookielib    
def Brower(url):    
    login_page = "http://pub.alimama.com"  
    login_data="usrname=admin&passwd=admin&isCookieEnable=1&action=on&wrong_passwd=%3C%21--invalid_passwd_flag--%3E" #get from fiddler  
    try:    
        cj = cookielib.CookieJar()    
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))    
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 8.0;\  
        Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152;\  
        .NET CLR 3.5.30729; MS-RTC LM 8; InfoPath.2; CIBA; .NET4.0C; .NET4.0E; .NET CLR 1.1.4322)')]  
          
        opener.open(login_page,login_data)    
        op=opener.open(url)    
        data= op.read()    
        return data    
    except Exception,e:   
        print str(e)    
print Brower("http://pub.alimama.com") 


#Python中通过urllib.unquote，可以解码出原始url地址
import urllib;
 
encodedUrl = "http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html";
decodedUrl = urllib.unquote(encodedUrl);
print "encodedUrl=\t%s\r\ndecodedUrl=\t%s"%(encodedUrl, decodedUrl);
#encodedUrl=     http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html
#decodedUrl=     <a href="http://www.baidu.com/cache/user/html/jump.html">http://www.baidu.com/cache/user/html/jump.html</a>


#Python相关函数：

#将空格编码为%20：urllib.quote
#urllib.quote(string[, safe])
#Replace special characters in string using the %xx escape. Letters, digits, and the characters '_.-' are never quoted. By default, this function is intended for quoting the path section of the URL. The optional safe parameter specifies additional characters that should not be quoted — its default value is '/'.

#Example: quote('/~connolly/') yields '/%7econnolly/'.

#将空格编码为加号’+’：urllib.quote_plus
#urllib.quote_plus(string[, safe])
#Like quote(), but also replaces spaces by plus signs, as required for quoting HTML form values when building up a query string to go into a URL. Plus signs in the original string are escaped unless they are included in safe. It also does not have safe default to '/'.

