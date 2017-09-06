#!/usr/bin/env python  
# -*- coding:utf-8 -*-

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

from ConfigParser import ConfigParser

class ConfigRunMode(object):
    def __init__(self, ini_file):
        self.ini_file = ini_file
        
        config = ConfigParser()
        #从配置文件中读取运行模式
        config.read(self.ini_file)
        
        self.run_mode = int(config.get('RUNCASECONFIG','runmode'))
        self.case_list = eval(config.get('RUNCASECONFIG','case_id'))
        
    def get_run_mode(self):
        return self.run_mode
    
    def get_case_list(self):
        return self.case_list   
