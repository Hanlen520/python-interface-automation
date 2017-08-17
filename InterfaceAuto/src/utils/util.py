#coding:utf-8

from Crypto.Cipher import AES
import json
import base64
from idlelib.IOBinding import encoding
 
class Crypt(object):
    def __init__(self,key,mode,iv):
        self.key = key
        self.mode = mode
        self.iv = iv
     
    #加密函数
    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode,self.iv)
        
    #如果text不足16位就用空格补足为16位，
    #如果大于16但不是16的倍数，那就补足为16的倍数。
        if len(text)<16:
            text = text + ('\0' * (16-len(text)))
        elif len(text)>=16:
            text = text + ('\0' * (16-(len(text)%16)))
            
        ciphertext = cryptor.encrypt(text)
        return base64.b64encode(ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,self.iv)
        ciphertext = base64.b64decode(text)
        plain_text  = cryptor.decrypt(ciphertext)
        return plain_text.rstrip("\0")
 
if __name__ == '__main__':
    pc = Crypt(mode=AES.MODE_CBC,key='d3YmI1BUOSE2S2YmalBVZUQ=',iv=b'0000000000000000')
    d = {"header":1}
    d = json.dumps(d)

    s_1 = pc.encrypt(d)
    
    print "加密后的字符串为：",s_1
    
    s_2 = pc.decrypt("8A4rXyzWhSx0xqFwHfDolw==")
    print "解密后的字符串为：",s_2
    

