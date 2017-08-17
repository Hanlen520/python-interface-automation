#coding:utf-8

'''
Created on 2016-11-2

@author: Sun Jinsen
'''

import unittest 

# 测试用例(组)类
class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', test_data=None, http=None, db_cursor=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.test_data = test_data
        self.http = http
        self.db_cursor = db_cursor


class TestInterfaceCase(ParametrizedTestCase):
    def setUp(self):
        pass

    def test_login(self):
        '''
        #添加HTTP请求头
        header = {
            'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 6.0; Letv X500 Build/DAXCNCU5801810201S)',
            'Content-Type':'application/x-www-form-urlencoded'
            }
        self.http.set_header(header)
        '''
        response = self.http.post(self.test_data.request_url, self.test_data.request_param)
        
        if {} == response:
            self.test_data.result = 'Error'
            try:
                # 更新结果表中的用例运行结果
                self.db_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s', (self.test_data.result, self.test_data.case_id))
                self.db_cursor.execute('commit')
            except Exception as e:
                print e
                self.db1_cursor.execute('rollback')
            return

        try:
            self.assertEqual(response['Code'], 0, msg=u'返回报文结果中Code不等于0' )
            self.test_data.result = 'Pass'
            
        except AssertionError as e:
            self.test_data.result = 'Fail'
            self.test_data.reason = '%s' % e # 记录失败原因

        # 更新结果表中的用例运行结果
        try:
            self.db_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s', (self.test_data.result, self.test_data.case_id))
            self.db_cursor.execute('commit')
                
            self.db_cursor.execute('UPDATE test_result SET reason = %s WHERE case_id = %s', (self.test_data.reason, self.test_data.case_id))
            self.db_cursor.execute('commit')
        except:
            self.db_cursor.execute('rollback')
 
    def tearDown(self):
        pass
