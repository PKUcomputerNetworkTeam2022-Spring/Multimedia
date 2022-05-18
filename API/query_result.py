#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from datetime import time
from .secret import get_token

# 查询音频任务转写结果请求地址
API_URL = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/query'

# 转写任务id列表，task_id是通过创建音频转写任务时获取到的，每个音频任务对应的值

def query_task(*tasks, path='output/output.txt'):
    body = {
        "task_ids": list(tasks),
    }

    params = {"access_token": get_token()}

    response = requests.post(API_URL, json=body, params=params)
    datas: dict = response.json()
    for tid, task in zip(tasks, datas['tasks_info']):
        if task['task_status'] != 'Success':
            print(f'task {tid} not finished: {task["task_status"]}')
            continue
        result: dict = task['task_result']
        if path is not None:
            try:
                with open(path, 'a', encoding='utf-8') as f:
                    f.write('\n'.join([
                        '-' * 10 + f'{tid}' + '-' * 10,
                        '\ttext:',
                        '\t' + result['result'][0],
                        '\tdetails:',
                        *[
                            '\t\t' + format_time(d['begin_time'])
                            + '-' + format_time(d['end_time'])
                            + '\n\t\t' + d['res'][0]
                            for d in result['detailed_result']],
                        '-' * 10 + f'{tid}' + '-' * 10,
                        '\n',
                    ]))
            except Exception as e:
                print(f'log failed for query_task({path=}): {e}')
    return response


def format_time(ms):
    s, ms = divmod(ms * 1000, 1000000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return str(time(h, m, s, ms))
