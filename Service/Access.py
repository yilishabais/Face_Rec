import os
import sys
import json
import base64
import requests


def Get_API():
    AK = 'rWHVG2KWFwZdRwThq6R1rGrt'
    SK = '7AYFcldBHx6Q3fenRbYXB4fVEGF2Gxk0'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        AK, SK)
    # 构造一个url对象 向服务器请求资源
    response = requests.get(host)
    if response:
        print(response.json())
    # 返回请求的值从中取出access_token
    access_token = eval(response.text)['access_token']
    # 人脸识别功能请求地址

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    API = request_url + "?access_token=" + access_token

    # 获取API
    return API


def img_64(img):
    f = open(r"%s" % img, "rb")
    pic = base64.b64encode(f.read())
    f.close()
    return pic


def de_img(img1, img2):
    # img base64 编码
    pic_1 = img_64(img1)
    pic_2 = img_64(img2)

    # 将对比图转换成json格式 具体链接看https://cloud.baidu.com/doc/FACE/s/Lk37c1tpf
    params = json.dumps([
        {"image": str(pic_1, "utf-8"), "image_type": 'BASE64',
         "face_type": "LIVE"},
        {"image": str(pic_2, "utf-8"), "image_type": 'BASE64', "face_type": "LIVE"}])

    return params


def result(img1, img2):
    api = Get_API()
    params = de_img(img1, img2)
    content = requests.post(api, params)
    socer = eval(content.text)["result"]["score"]
    socer = round(socer,2)
    if socer >= 80:
        return True
    else:
        return False


