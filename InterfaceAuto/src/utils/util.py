#!/usr/bin/env python  
# -*- coding:utf-8 -*-   
   
from Crypto.Cipher import AES  
import json
import base64
   
class prpcrypt():  
    def __init__(self,key,iv):  
        self.key = key  
        self.iv  = iv  
        self.mode = AES.MODE_CBC  
        self.BS = AES.block_size  
        #补位  
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)   
        self.unpad = lambda s : s[0:-ord(s[-1])]  
       
    def encrypt(self,text):
        text = self.pad(text)  
        cryptor = AES.new(self.key,self.mode,self.iv)
        ciphertext = cryptor.encrypt(text)
        #把加密后的字符串转化为base64字符串  
        return base64.b64encode(ciphertext)  
       
    #解密后，去掉补足的空格rstrip()
    def decrypt(self,text):  
        cryptor = AES.new(self.key,self.mode, self.iv)  
        plain_text  = cryptor.decrypt(base64.b64decode(text))  
        return self.unpad(plain_text.rstrip('\0'))  
       
if __name__ == '__main__':  
    pc = prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=','0000000000000000') #初始化密钥和iv

    pre_dict = {
        "header":{
            "appVersion":"3.8.8",
            "cmdID":"1173636",
            "platformVersion":"5.0.2",
            "action":"1011",
            "cmdName":"app_wdj",
            "userType":1,
            "userID":"",
            "uuid":"ffffffff-cb8f-179a-5297-397b0033c587",
            "platformCode":"Android",
            "phoneName":"Xiaomi",
            "token":""
            },
        "body":"{\"name\":\"15122223333\",\"pw\":\"aaaaaa\",\"usertype\":\"1\"}"
        }

    dict_to_json = json.dumps(pre_dict, sort_keys=True)
    
    e = pc.encrypt(dict_to_json) #加密
    
    d = pc.decrypt(e) #解密  
    print u"加密:",e  
    print u"解密:",d
