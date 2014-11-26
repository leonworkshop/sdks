#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2013-12-20

@author: stanleyzeng
'''

import xinge
import json

#xinge.XingeHelper.SetServer('10.213.110.4')
#xinge.XingeHelper.SetServer('10.213.166.139')
#xinge.XingeHelper.SetServer('10.213.166.176')
#xinge.XingeHelper.SetServer('10.166.224.41')
#xinge.XingeHelper.SetServer('10.128.67.229')

def TestPushToken():
    x = xinge.XingeApp(353, '353_secret_key')
    x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = xinge.XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = xinge.XingeApp(2100000105, '8131855e542e676348d77e4fbb7f58d3')
    #x = xinge.XingeApp(2100026643, 'e2f24b5f152122d15eba29ca375a8111')
    #x = xinge.XingeApp(2100038814, '74e636481463b7d57ea04956c096c4b4')
    #x = xinge.XingeApp(2190000354, 'xg354key')
    #x = xinge.XingeApp(2100037277, 'b608ae581db4773be3859efe8e05e9b5')
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_MESSAGE
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = '中文标题按token'
    msg.content = '中文内容，これは中国である'
    msg.content = 'aaa啊こ'
    msg.content = '来自信鸽后台的测试消息'
    #msg.content = '{"content":{"aps":{"title":"\u5fae\u4fe1\u516c\u4f17\u53f7\u5f71\u54cd\u529b\u6392\u884c\u699c\u53d1\u5e03","alert":"\u4e0e\u624b\u673a\u79fb\u52a8\u7b49\u65b0\u5a92\u4f53\u76f8\u6bd4\uff0c\u4ee5\u62a5\u7eb8\u4e3a\u4ee3\u8868\u7684\u4f20\u7edf\u5a92\u4f53\uff0c\u6108\u52a0\u5b64\u5bc2\u4e0e\u6ca1\u843d\u3002","contentid":"959","modelid":"1"}}}'
    #msg.content = '中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文中文'
    #msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.sendTime = '2014-07-31 18:21:00'
    msg.expireTime = 86400
    #msg.multiPkg = xinge.Message.PUSH_ACCESS_ID

    ti = xinge.TimeInterval(20, 22, 23, 0)
    #msg.acceptTime = (ti,)

    #style = xinge.Style(2, 1, 1, 1)
    style = xinge.Style(0, 0, 0, 1)
    msg.style = style
    
    action = xinge.ClickAction()
    #action.actionType = xinge.ClickAction.TYPE_URL
    action.actionType = 4
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action
    
    ret = x.PushSingleDevice('16f4f363697c09a84642ab9145fae91bb46a223a', msg, xinge.XingeApp.ENV_DEV)
    #ret = x.PushSingleDevice('99e93efde5d8f9d248e6be4ee9df8a8665b52716', msg, xinge.XingeApp.ENV_DEV)
    
    print ret

def TestPushTokenIos():
    x = xinge.XingeApp(101, 'skey')
    #x = xinge.XingeApp(2200002956, '1f0d10a3589de22a9fbd84e011ba126f')
    #x = xinge.XingeApp(2100001657, 'd89db8f08a067b39f85729779423bdba')
    x = xinge.XingeApp(2290000353, 'key2')
    #msg = xinge.Message()
    msg = xinge.MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    #msg.alert = '==================================================================================================================================================================================================================================================='
    #msg.alert = '我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字我是五个字'
    #msg.alert = '555555555'
    #msg.badge = 5
    #msg.sound = 'ooo.wav'
    #msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = xinge.TimeInterval(17, 0, 23, 0)
    #msg.acceptTime = (ti,)
    
    ret = x.PushSingleDevice('56abe79fd5424a7a10575c4b49144de46886bffdb0a5fcb4a78a8b0a145305cc', msg, xinge.XingeApp.ENV_DEV)
    
    print ret

def TestPushAccount():
    x = xinge.XingeApp(100, 'key2')
    #x = xinge.XingeApp(2100006809, '464e63738779a9267a39888885c8e047')
    #x = xinge.XingeApp(2100000098, 'a45f4de4867db037b48b5bf8e31074c1')
    #x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = xinge.XingeApp(2100001818, 'a35c330adba92477ce300ed885533193')
    #x = xinge.XingeApp(2100032013, '36bff1cf1f53bdfce28e3c8eeeac6b2b')
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_MESSAGE
    msg.type = xinge.Message.TYPE_NOTIFICATION
    #msg.title = '中文标题全部设备'
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.expireTime = 300
    #msg.sendTime = '2014-01-10 17:30:00'
    #msg.multiPkg = xinge.Message.PUSH_ACCESS_ID

    ti = xinge.TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = xinge.Style(2, 1, 1, 1) 
    msg.style = style
    
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.actionType = xinge.ClickAction.TYPE_ACTIVITY
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ################################
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = 'some title stanley'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，非必须
    #msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，key和value都必须是字符串，非必须
    msg.custom = {'aaa':'111', 'bbb':'222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    #msg.multiPkg = 1
    
    # 允许推送时段设置，非必须
    #ti1 = xinge.TimeInterval(9, 30, 11, 30)
    #ti2 = xinge.TimeInterval(14, 0, 17, 0)
    #msg.acceptTime = (ti1, ti2)
    
    # 通知展示样式，仅对通知有效
    # 样式编号为2，响铃，震动，不可从通知栏清除，不影响先前通知
    style = xinge.Style(2, 1, 1, 0, 0)
    msg.style = style
    
    # 点击动作设置，仅对通知有效
    # 以下例子为点击打开url
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    # 打开url不需要用户确认
    action.confirmOnUrl = 0
    msg.action = action
    
    ret = x.PushSingleAccount(xinge.XingeApp.DEVICE_ALL, '241008', msg, 0)
    
    print ret
    
def TestPushAccountIos():
    x = xinge.XingeApp(101, 'skey')
    msg = xinge.MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    msg.badge = 5
    msg.sound = 'default'
    msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = xinge.TimeInterval(17, 0, 23, 0)
    #msg.acceptTime = (ti,)
    
    ret = x.PushSingleAccount(xinge.XingeApp.DEVICE_ALL, '123456', msg, xinge.XingeApp.ENV_DEV)
    
    print ret

def TestPushAccountList():
    #x = xinge.XingeApp(100, 'key2')
    #x = xinge.XingeApp(2100006809, '464e63738779a9267a39888885c8e047')
    #x = xinge.XingeApp(2100000098, 'a45f4de4867db037b48b5bf8e31074c1')
    #x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = xinge.XingeApp(2100001818, 'a35c330adba92477ce300ed885533193')
    #x = xinge.XingeApp(2100032013, '36bff1cf1f53bdfce28e3c8eeeac6b2b')
    x = xinge.XingeApp(353, '353_secret_key')
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_MESSAGE
    msg.type = xinge.Message.TYPE_NOTIFICATION
    #msg.title = '中文标题全部设备'
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    msg.expireTime = 300
    #msg.sendTime = '2014-01-10 17:30:00'
    #msg.multiPkg = xinge.Message.PUSH_ACCESS_ID

    ti = xinge.TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = xinge.Style(2, 1, 1, 1) 
    msg.style = style
    
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.actionType = xinge.ClickAction.TYPE_ACTIVITY
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

    ################################
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = 'some title stanley'
    msg.content = 'some content'
    # 消息为离线设备保存的时间，单位为秒。默认为0，表示只推在线设备
    msg.expireTime = 86400
    # 定时推送，非必须
    #msg.sendTime = '2012-12-12 18:48:00'
    # 自定义键值对，key和value都必须是字符串，非必须
    msg.custom = {'aaa':'111', 'bbb':'222'}
    # 使用多包名推送模式，详细说明参见文档和wiki，如果您不清楚该字段含义，则无需设置
    #msg.multiPkg = 1
    
    # 允许推送时段设置，非必须
    #ti1 = xinge.TimeInterval(9, 30, 11, 30)
    #ti2 = xinge.TimeInterval(14, 0, 17, 0)
    #msg.acceptTime = (ti1, ti2)
    
    # 通知展示样式，仅对通知有效
    # 样式编号为2，响铃，震动，不可从通知栏清除，不影响先前通知
    style = xinge.Style(2, 1, 1, 0, 0)
    msg.style = style
    
    # 点击动作设置，仅对通知有效
    # 以下例子为点击打开url
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    # 打开url不需要用户确认
    action.confirmOnUrl = 0
    msg.action = action
    
    accountList = list()
    accountList.append('250708811')
    accountList.append('250708811')
    accountList.append('250708811')
    accountList.append('250708810')
    
    ret = x.PushAccountList(xinge.XingeApp.DEVICE_ALL, accountList, msg, 0)
    
    print ret
    
def TestPushAccountListIos():
    x = xinge.XingeApp(101, 'skey')
    msg = xinge.MessageIOS()
    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
    msg.alert = 'gogogo'
    msg.badge = 5
    msg.sound = 'default'
    msg.custom['aa'] = 'sssss'
    #msg.sendTime = '2014-03-12 18:21:00'
    ti = xinge.TimeInterval(17, 0, 23, 0)
    #msg.acceptTime = (ti,)
    
    accountList = list()
    accountList.append('123456')
    accountList.append('123456')
    accountList.append('12346')
    
    ret = x.PushAccountList(xinge.XingeApp.DEVICE_ALL, accountList, msg, xinge.XingeApp.ENV_DEV)
    
    print ret
    
def TestPushAll():
    x = xinge.XingeApp(100, 'key2')
    x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    #x = xinge.XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = xinge.XingeApp(2100036917, 'c35a0de6e38ecb0981863d7d796b8078')
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_MESSAGE
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = '中文标题ALL'
    msg.content = '中文内容，これは中国である'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    #msg.sendTime = '2014-01-15 14:19:00'
    #msg.multiPkg = xinge.Message.PUSH_ACCESS_ID

    ti = xinge.TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = xinge.Style(2, 1, 1, 1) 
    msg.style = style
    
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    msg.action = action

##    x = xinge.XingeApp(2200002833, 'bc8772dca4a3bed8d1312aecad6a8464')
##    msg = xinge.MessageIOS()
##    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
##    msg.alert = 'gogogo'
##    msg.alert = '================================================================================================================================================================================================'
##    #msg.alert = '555555555'
##    msg.badge = 5
##    msg.sound = 'ooo.wav'
##    msg.custom['aa'] = 'sssss'
##    #msg.sendTime = '2014-03-12 18:21:00'
##    ti = xinge.TimeInterval(17, 0, 23, 0)
##    msg.acceptTime = (ti,)
    
    ret = x.PushAllDevices(xinge.XingeApp.DEVICE_ALL, msg)
    
    print ret

def TestPushTags():
    x = xinge.XingeApp(100, 'key2')
    x = xinge.XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    #x = xinge.XingeApp(2100022134, '84d4a95bae4ae9ad2286db85d4d4c72a')
    msg = xinge.Message()
    msg.type = xinge.Message.TYPE_MESSAGE
    msg.type = xinge.Message.TYPE_NOTIFICATION
    msg.title = 'hi信鸽'
    msg.content = 'hi信鸽'
    msg.custom = {'aaa':'111', 'bbb':'222'}
    #msg.sendTime = '2014-01-15 14:19:00'
    #msg.multiPkg = xinge.Message.PUSH_ACCESS_ID

    ti = xinge.TimeInterval(8, 0, 23, 0)
    #msg.acceptTime = (ti,)

    style = xinge.Style(2, 1, 1, 1) 
    msg.style = style
    
    action = xinge.ClickAction()
    action.actionType = xinge.ClickAction.TYPE_URL
    action.url = 'http://xg.qq.com'
    action.confirmOnUrl = 1
    #msg.action = action

##    x = xinge.XingeApp(2200002833, 'bc8772dca4a3bed8d1312aecad6a8464')
##    msg = xinge.MessageIOS()
##    #msg.raw = "{\"aps\":{\"alert\":\"Hello world--joelliu!!! message from c++\",\"badge\":1}}"
##    msg.alert = 'gogogo'
##    msg.alert = '================================================================================================================================================================================================'
##    msg.alert = '555555555'
##    msg.badge = 5
##    msg.sound = 'ooo.wav'
##    msg.custom['aa'] = 'sssss'
##    msg.sendTime = '2014-03-12 18:21:00'
##    ti = xinge.TimeInterval(17, 0, 23, 0)
##    #msg.acceptTime = (ti,)
    
    ret = x.PushTags(xinge.XingeApp.DEVICE_ALL, ('bbb',), 'OR', msg)
    
    print ret
    
def TestQueryPushStatus():
    x = xinge.XingeApp(100, 'key2')
    x = xinge.XingeApp(2100001810, '16c2fd6e0f2204ff2e2779e81709674b')
    ret = x.QueryPushStatus(('13101','14067'))
    print ret
    #print ret[2]['30']
    
def TestQueryDeviceNum():
    x = xinge.XingeApp(100, 'key2')
    #x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    x = xinge.XingeApp(2100012989, '8eb70727b2caae06f3d05b85df95c7cb')
    x = xinge.XingeApp(2100002214, 'e863ea9c8088db3cd8f2a9074f704a18')
    ret = x.QueryDeviceCount()
    print ret
    
def TestQueryTags():
    x = xinge.XingeApp(353, '353_secret_key')
    #x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    x = xinge.XingeApp(2100012989, '8eb70727b2caae06f3d05b85df95c7cb')
    ret = x.QueryTags(0, 50)
    print ret
    
def TestCancelTimingPush():
    x = xinge.XingeApp(100, 'key2')
    #x = xinge.XingeApp(2100000097, '50f3b708dc241503484c80996c3e46b3')
    ret = x.CancelTimingPush('15')
    print ret

def TestBatchSetTag():
    x = xinge.XingeApp(353, '353_secret_key')
    x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    pairs = [xinge.TagTokenPair(('tag%d' % i),'16ec008f123a7b444161a113f25c7ebcf0df1b09') for i in range(20)]    #pairs = []
    ret = x.BatchSetTag(pairs)
    print ret

def TestBatchDelTag():
    x = xinge.XingeApp(353, '353_secret_key')
    x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    pairs = [xinge.TagTokenPair(('tag%d' % i),'16ec008f123a7b444161a113f25c7ebcf0df1b09') for i in range(20)]
    ret = x.BatchDelTag(pairs)
    print ret

def TestQueryTokenTags():
    x = xinge.XingeApp(353, '353_secret_key')
    #x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    ret = x.QueryTokenTags('16ec008f123a7b444161a113f25c7ebcf0df1b09')
    print ret

def TestQueryTagTokenNum():
    x = xinge.XingeApp(353, '353_secret_key')
    x = xinge.XingeApp(2100001752, '7c526a5e2ff5b61f4f635c1b0b86214b')
    ret = x.QueryTagTokenNum('tag1')
    print ret

if '__main__' == __name__:
    TestPushToken()
    #TestPushTokenIos()
    #TestPushAccount()
    #TestPushAccountIos()
    #TestPushAccountList()
    #TestPushAccountListIos()
    #TestPushAll()
    #TestPushTags()
    #TestQueryPushStatus()
    #TestQueryDeviceNum()
    #TestQueryTags()
    #TestCancelTimingPush()
    #TestBatchSetTag()
    #TestBatchDelTag()
    #TestQueryTokenTags()
    #TestQueryTagTokenNum()
    

