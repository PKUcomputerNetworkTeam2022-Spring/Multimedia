#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from API.secret import get_token

API_URL = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/create'

'''
ffmpeg可参考https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf
音频格式转化可通过开源ffmpeg工具或音频处理软件
'''

def create_task(url, format='wav', pid=80001):
    body = {
        "speech_url": url,
        "format": format,   # 音频格式，支持pcm,wav,mp3等
        "pid": pid,         # 模型pid，1537为普通话输入法模型，1737为英语模型，80001为中文语音近场识别模型极速版
        "rate": 16000,      # 音频采样率，支持16000采样率
    }
    params = {"access_token": get_token()}
    response = requests.post(API_URL, json=body, params=params)

    # 返回请求结果信息，获得task_id，通过识别结果查询接口，获取识别结果
    print(response.text)
    try:
        with open('output/tasks.log', 'a') as f:
            f.write(f'create_task({url=}, {format=}, {pid=}):\n')
            f.write('\t')
            f.write(response.text)
            f.write('\n\n')
    except:
        print(f'log failed for create_task({url=}, {format=}, {pid=})')
    return response
