import time
import hashlib
import base64
import hmac
import requests
from datetime import datetime


class FeishuRobot(object):

    def __init__(self):
        self.__webhook = 'https://open.feishu.cn/open-apis/bot/v2/hook/c4dac0db-88d4-4225-9f68-1bbcca03c946'
        self.__secret_key = 'dYife2uPknIWUBe0WM0M0f'

    def send_text_msg(self, text):
        timestamp = int(time.time())
        data = {
            'timestamp': timestamp,
            'sign': self.gen_sign(timestamp, self.__secret_key),
            'msg_type': 'text',
            'content': {'text': text}
        }
        print(data)
        resp = requests.post(url=self.__webhook, json=data)
        print(resp.text)

    @staticmethod
    def gen_sign(timestamp, secret):
        # 拼接timestamp和secret
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign


if __name__ == '__main__':
    robot = FeishuRobot()
    robot.send_text_msg('request example')
