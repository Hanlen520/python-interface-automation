#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

import urllib
import urllib2
import cookielib

import json
from ConfigParser import ConfigParser

#配置类
class ConfigHttp(object):
    '''配置要测试借口服务器的IP、PORT、HOST等信息，封装http请求方法'''
    
    def __init__(self, ini_file):
        config = ConfigParser()
        
        #从配置文件中读取借口服务器的IP、端口、域名
        config.read(ini_file)
        
        self.host = config.get('HTTP', 'host')
        self.port = config.get('HTTP', 'port')
        
        self.headers = {}
        
        #请求带有Cookie
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        
    def set_host(self, host):
        self.host = host
        
    def get_host(self):
        return self.host
    
    def set_port(self, port):
        self.port = port
        
    def get_port(self):
        return self.port
    
    def set_header(self, headers):
        self.headers = headers
        
    #封装GET方法
    def get(self, url, params):
        params = urllib.urlencode(params)
        
#         print params
        
        url = 'http://' + self.host + url + '?' + params
        
        request = urllib2.Request(url, headers = self.headers)
        
        try:
            repsonse = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            print e.code
            return {}
        except urllib2.URLError, e:
            print e.reason
            return {}
        else:
            response = repsonse.read()
            json_response = json.loads(response)  
            return json_response
    
    #封装POST方法    
    def post(self, url, params):
        params = urllib.urlencode(params)
        
#         print params

        url = 'http://' + self.host + url
        request = urllib2.Request(url, params, headers = self.headers)
        
        try:
            repsonse = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            print e.code
            return {}
        except urllib2.URLError, e:
            print e.reason
            return {}
        else:
            response = repsonse.read()
            json_response = json.loads(response)  
            return json_response