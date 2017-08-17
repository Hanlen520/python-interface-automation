#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

import datetime
import unittest

from interface.runcase import RunCase
from interface.globalconfig import GlobalConfig
from interface.htmlreport import HtmlReport

import sys                        

reload(sys) 
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    
    # 记录测试开始时间
    start_time = datetime.datetime.now()

    # 全局配置
    global_config = GlobalConfig()
    
    run_mode = global_config.get_run_mode()                 # 运行模式
    run_case_list = global_config.get_run_case_list()         # 需要运行的用例列表
    db_conn = global_config.get_db_conn()                   # 连接测试数据库             # 测试环境数据库连接
    http = global_config.get_http()                                  # 连接http接口

    # 运行测试用例
    runner = unittest.TextTestRunner()
    case_runner = RunCase()
    case_runner.run_case(runner, run_mode, run_case_list, db_conn, http)

    # 记录测试结束时间
    end_time = datetime.datetime.now()

    # 构造测试报告
    html_report = HtmlReport(db_conn.cursor())
    
    # 计算测试消耗时间
    html_report.set_time_took(str(end_time - start_time)) 

    # 生成测试报告
    html_report.generate_html('test report', './report/report.html')

    # 释放数据库连接资源
    global_config.clear()