# -*- coding:utf8 -*-
# -*- author:xiaoxiang -*-

import json
import os
import requests

class sign():
    def __init__(self):
        self.count = 1
        self.url = "https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign"
        self.text = "直播签到"
        self.content = []

    def DoSign(self,value,server):
        for cookie in value:
            header = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie':f"{cookie}",
                'origin': 'https://link.bilibili.com',
                'referer': 'https://link.bilibili.com/p/center/index?visit_id=5zqfc2op2h80',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                }
            result = requests.get(url=self.url,headers=header)
            js = json.loads(result.text)
            if js.get("message")=="0":
                print("帐号"+f"{self.count}"+"签到结果：成功,获得奖励"+js.get("data").get("text"))
                self.content.append("帐号"+f"{self.count}"+"签到结果：成功,获得奖励"+js.get("data").get("text"))
            else:
                print("帐号"+f"{self.count}"+"签到结果："+js.get("message"))
                self.content.append("帐号"+f"{self.count}"+"签到结果："+js.get("message"))
            self.count = self.count + 1
        if(server!=None):
            s_url="https://sc.ftqq.com/"+server+".send"
            data = {
                "text":self.text,
                "desp":"******".join(self.content)
            }
            print(s_url)
            response = requests.post(url=s_url,data=data)
            print(response.text)

def main_handler(event, context):
    value = os.environ.get("COOKIE").split("#")
    the_sign = sign()
    the_sign.DoSign(value,os.environ.get("SERVER"))