import base64
import json
import requests

debug_print = print

# 填写百度控制台中相关开通了“音频文件转写”接口的应用的的API_KEY及SECRET_KEY
API_KEY = '****'
SECRET_KEY = '****'

TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
# SCOPE = 'brain_bicc'  # 有此scope表示有asr能力，没有请在网页里勾选 bicc
SCOPE = 'brain_asr_async'  # 有此scope表示有asr能力，没有请在网页里勾选
# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有asr能力，没有请在网页里勾选

_token = None


def set_debug(debug: bool):
    global debug_print
    if debug:
        debug_print = print
    else:
        debug_print = lambda *args, **kwargs: None


def get_token(refresh=True):
    if _token is None and refresh:
        fetch_token()
    return _token


def read_config(json_path='./API/config.json'):
    global API_KEY, SECRET_KEY
    try:
        with open(json_path, 'r') as f:
            config: dict = json.load(f)
        API_KEY = config['key']
        SECRET_KEY = config['secret']
        print('Config loaded')
    except:
        print(f'Config file "{json_path}" not found')


# 通过开通音频文件转写接口的百度应用的API_KEY及SECRET_KEY获取请求token
def fetch_token():
    global _token
    if API_KEY.startswith('*'):
        read_config()
    params = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET_KEY,
    }
    try:
        response = requests.post(TOKEN_URL, params=params)
        response.raise_for_status()
        result: dict = response.json()
    except Exception as e:
        debug_print(e)
        return

    debug_print(result)
    if 'access_token' in result.keys() and 'scope' in result.keys():
        if not SCOPE in result['scope'].split(' '):
            raise ValueError('scope is not correct')
        debug_print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' %
                    (result['access_token'], result['expires_in']))
        _token = result['access_token']
        return _token
    else:
        raise ValueError('MAYBE API_KEY or SECRET_KEY not correct: ' +
                         'access_token or scope not found in token response')
