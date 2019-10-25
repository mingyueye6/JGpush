# coding: utf-8

import base64
import json

import requests as requests

AppKey = '0759ed62896a93adf0aca137'
MasterSecret = 'f30b3ce52cc6c5a55ed3e5a0'


def jp_push(peoples, voice_str, sound):
    # peoples 推送到某个/某些用户，列表
    # voice_str 推送的内容
    # sound 需要播放的声音文件
    url = "https://api.jpush.cn/v3/push"
    if peoples:
        audience = {"registration_id": peoples}
    else:
        audience = "all"
    if sound:
        sound = str(sound) + '.mp3'
    else:
        sound = "default"

    req_data = {
        "audience": audience,
        "platform": "all",
        "options": {"time_to_live": 86400, "apns_production": False},  # apns_production 线上环境为True
        "notification": {
            "ios": {
                "alert": voice_str,
                "sound": sound,
                "badge": "+1",
                "extras": {
                    "content": {
                        "file": sound,
                    }
                }
            },
            "android": {
                "alert": voice_str,
                "extras": {
                    "content": {
                        "file": sound,
                    }
                }
            }
        }
    }
    str_code = "{}:{}".format(AppKey, MasterSecret)
    signature = base64.b64encode(str_code.encode('utf8')).decode()
    headers = {"Content-Type": "application/json", "Authorization": "Basic {}".format(signature)}
    resp = requests.post(url, data=json.dumps(req_data), headers=headers)
    resp.encoding = 'utf-8'
    body = resp.json()
    print(body)



if __name__ == '__main__':
    jp_push('', '', '')