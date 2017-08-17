#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

import unittest
from test_interface_case import TestInterfaceCase
from datastruct import DataStruct

global test_data
test_data = DataStruct()

class RunCase(object):
    '''运行测试用例'''

    def __init__(self):
        pass

    # 运行测试用例函数
    def run_case(self, runner, run_mode, run_case_list, db_conn, http):
        global test_data
        db_cursor = db_conn.cursor()
        
        if 1 == run_mode:  # 运行全部用例
            # 获取用例个数
            db_cursor.execute('SELECT count(case_id) FROM test_data')
            test_case_num = db_cursor.fetchone()[0]

            # 循环执行测试用例
            for case_id in range(1, test_case_num+1):
                db_cursor.execute('SELECT  http_method, request_name, request_url, request_param, test_method, test_desc, action FROM test_data WHERE case_id = %s',(case_id,))
                # 记录数据
                tmp_result = db_cursor.fetchone()
                
                test_data.case_id = case_id
                test_data.http_method = tmp_result[0].encode("utf-8")
                test_data.request_name = tmp_result[1].encode("utf-8")
                test_data.request_url = tmp_result[2].encode("utf-8")
                test_data.request_param = tmp_result[3].encode("utf-8")
                test_data.test_method = tmp_result[4].encode("utf-8")
                test_data.test_desc = tmp_result[5].encode("utf-8")
                test_data.action = tmp_result[6].encode("utf-8")    
                test_data.result = ''
                test_data.reason = ''
                
#                import pdb
#                pdb.set_trace()
                    
                try:
                    sql = 'INSERT INTO test_result (case_id, http_method, request_name, request_url,request_param, test_method, test_desc, action, result, reason) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    data = (test_data.case_id, test_data.http_method, test_data.request_name, test_data.request_url, 
                            test_data.request_param, test_data.test_method, test_data.test_desc, test_data.action, test_data.result, test_data.reason)
                    
                    db_cursor.execute(sql,data)
                    db_conn.commit()
                except:
                    # 回滚
                    db_conn.rollback()

                test_suite = unittest.TestSuite()
                test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db_cursor))
                runner.run(test_suite)
        else:   # 运行部分用例
            
            # 循环执行测试用例
            for case_id in run_case_list:
                db_cursor.execute('SELECT http_method, request_name, request_url, request_param, test_method, test_desc ''FROM test_data WHERE case_id = %s',(case_id,))
                # 记录数据
                tmp_result = db_cursor.fetchone()
                test_data.case_id = case_id
                test_data.http_method = tmp_result[0].encode("utf-8")
                test_data.request_name = tmp_result[1].encode("utf-8")
                test_data.request_url = tmp_result[2].encode("utf-8")
                test_data.request_param = tmp_result[3].encode("utf-8")
                test_data.test_method = tmp_result[4].encode("utf-8")
                test_data.test_desc = tmp_result[5].encode("utf-8")
                test_data.result = ''
                test_data.reason = ''

                try:
                    sql = 'INSERT INTO test_result(case_id, http_method, request_name, request_url,request_param, test_method, test_desc, result, reason) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'

                    data = (test_data.case_id,test_data.http_method,test_data.request_name, test_data.request_url,
                            test_data.request_param, test_data.test_method, test_data.test_desc,test_data.result, test_data.reason)
                    db_cursor.execute(sql, data)
                    
                    db_conn.commit()
                except:
                    # 回滚
                    db_conn.rollback()
                    
                test_suite = unittest.TestSuite()
                test_suite.addTest(TestInterfaceCase(test_data.test_method, test_data, http, db_cursor))
                runner.run(test_suite)
                
        db_cursor.close()