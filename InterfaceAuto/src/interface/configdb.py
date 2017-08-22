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
    def __init__(self, ini_file, db):
        self.ini_file = ini_file
        self.db = db
        
        config = ConfigParser()
        #从配置文件中读取数据库服务器ip,域名，端口
        config.read(self.ini_file)
        
        self.host = config.get(self.db,'host')
        self.port = config.get(self.db,'port')
        self.user = config.get(self.db,'user')
        self.passwd = config.get(self.db,'password')
        self.db = config.get(self.db,'db')
        self.charset = config.get(self.db,'charset')

    def get_conn(self):
        try:
            conn = connector.connect(host=self.host, port=self.port, user=self.user, password=self.passwd, database=self.db, charset=self.charset)
            return conn
        except Exception as e:
            print e
            sys.exit()
