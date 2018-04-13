# -*- coding:utf-8 -*-
#Author：叶国坚


import socket
import string
import time
import random
import requests
import string
import json
import hashlib
import xmltodict
import sys
import urllib
# import urllib2
import re

class PayToolUtil(object):

    # ========支付相关配置信息===========
    _APP_ID = "wx0f4bd126b3f2e340";  # 公众账号appid
    _MCH_ID = "1500093562";  # 商户号
    _API_KEY = "a959c511c41c4b6cbb221caf58bf993e";  # key设置路径：微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置

    # 有关url
    _host_name = socket.gethostname()
    _ip_address = socket.gethostbyname(_host_name)
    _CREATE_IP = _ip_address;  # 发起支付的ip
    
    _UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder";  #url是微信下单api 
    _NOTIFY_URL = "your Ip：端口／处理方法路径";  # 微信支付结果回调的处理方法


    def getPayUrl(self,orderid,goodsName,goodsPrice,**kwargs):
        '''
        向微信支付端发出请求，获取url
        '''
        
        appid = self._APP_ID
        mch_id = self._MCH_ID
        key = self._API_KEY
        nonce_str = str(int(round(time.time() * 1000)))+str(random.randint(1,999))+string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 5)).replace(" ","") #生成随机字符串
        spbill_create_ip = self._CREATE_IP
        notify_url = self._NOTIFY_URL
        trade_type = "NATIVE"

        params = {}
        params['appid'] = appid
        params['mch_id'] = mch_id
        params['nonce_str'] = nonce_str
        params['out_trade_no'] = orderid.encode('utf-8')    #客户端生成并传过来，参数必须用utf8编码，否则报错
        params['total_fee'] = goodsPrice   #单位是分，必须是整数
        params['spbill_create_ip'] = spbill_create_ip
        params['notify_url'] = notify_url
        params['body'] = goodsName.encode('utf-8')   #中文必须用utf-8编码，否则xml格式错误
        params['trade_type'] = trade_type

        #生成签名
        ret = []
        for k in sorted(params.keys()):
            if (k != 'sign') and (k != '') and (params[k] is not None):
                ret.append('%s=%s' % (k, params[k]))
        params_str = '&'.join(ret)
        params_str = '%(params_str)s&key=%(partner_key)s'%{'params_str': params_str, 'partner_key': key}
        #这里需要设置系统编码为utf-8，否则下面md5加密会报参数错误
        reload(sys)
        sys.setdefaultencoding('utf8')
        params_str = hashlib.md5(params_str.encode('utf-8')).hexdigest()
        sign = params_str.upper()
        params['sign'] = sign


        #拼接参数的xml字符串
        request_xml_str = '<xml>'
        for key, value in params.items():
            if isinstance(value, basestring):
                request_xml_str = '%s<%s><![CDATA[%s]]></%s>' % (request_xml_str, key, value, key, )
            else:
                request_xml_str = '%s<%s>%s</%s>' % (request_xml_str, key, value, key, )
        request_xml_str = '%s</xml>' % request_xml_str

        #向微信支付发出请求，并提取回传数据
        res = urllib2.Request(self._UFDODER_URL, data=request_xml_str)
        res_data = urllib2.urlopen(res)#打开响应流
        res_read = res_data.read()#读取响应流中数据
        doc = xmltodict.parse(res_read)#数据是xml格式的，转为dict
        return_code = doc['xml']['return_code'] #根据dict的层级，从顶层开始逐级访问提取所需内容
        if return_code=="SUCCESS":
            result_code = doc['xml']['result_code']
            if result_code=="SUCCESS":
                code_url = doc['xml']['code_url']
                return code_url
            else:
                err_des = doc['xml']['err_code_des']
                print ("errdes==========="+err_des)
        else:
            fail_des = doc['xml']['return_msg']
            print ("fail des============="+fail_des)
















