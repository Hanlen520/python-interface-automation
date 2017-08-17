#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

class DataStruct(object):
    def __init__(self):
        self.case_id = 0       #用例ID
        self.http_method = ''  #接口http方法
        self.request_name = '' #接口名
        self.request_url = ''  #接口请求url
        self.request_param = ''#请求参数体
        self.test_method = ''  #测试方法
        self.test_desc = ''    #测试用例描述
        self.result = ''       #测试结果
        self.reason = ''       #失败原因