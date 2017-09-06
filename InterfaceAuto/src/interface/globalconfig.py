#!/usr/bin/env python  
# -*- coding:utf-8 -*-

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

from confighttp import ConfigHttp
from configrunmode import ConfigRunMode
from configdb import ConfigDB

class GlobalConfig(object):
    def __init__(self):
        #读取并配置接口服务器ip，端口等信息
        self.http = ConfigHttp('D:/eclipse-workspace/InterfaceAuto/src/interface/http_config.ini')
#        print self.http
        
        #读取并配置数据库服务器ip，端口等信息
        self.db = ConfigDB('D:/eclipse-workspace/InterfaceAuto/src/interface/db_config.ini', 'DATABASE1')
        
        #读取运行模式
        self.run_mode = ConfigRunMode('D:/eclipse-workspace/InterfaceAuto/src/interface/case_config.ini')
        
    def get_http(self):
        return self.http

    # 返回本地数据库连接
    def get_db_conn(self):
        return self.db.get_conn()

    # 获取运行模式配置
    def get_run_mode(self):
        return self.run_mode.get_run_mode()

    # 获取需要单独运行的用例列表
    def get_run_case_list(self):
        return self.run_mode.get_case_list()
    
    #释放本地数据库连接资源
    def clear(self):
        self.db.get_conn().close()
