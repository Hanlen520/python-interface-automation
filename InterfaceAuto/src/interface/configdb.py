#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

from ConfigParser import ConfigParser
from mysql import connector
import sys

class ConfigDB(object):
    '''配置数据库ip，端口等信息，获取数据库连接'''
    def __init__(self, ini_file):
        config = ConfigParser()
        
        #从配置文件中读取数据库服务器ip,域名，端口
        config.read(ini_file)
        
        self.host = config.get('DATABASE1','host')
        self.port = config.get('DATABASE1','port')
        self.user = config.get('DATABASE1','user')
        self.passwd = config.get('DATABASE1','password')
        self.db = config.get('DATABASE1','db')
        self.charset = config.get('DATABASE1','charset')

    def get_conn(self):
        try:
            conn = connector.connect(host=self.host, port=self.port, user=self.user, password=self.passwd, database=self.db, charset=self.charset)
            return conn
        except Exception as e:
            print e
            sys.exit()
