from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


'''
class ChatConsumer(WebsocketConsumer):
    
    def websocket_connect(self, message):
        # 接受客户端的连接
        self.group_id = self.scope['url_route']['kwargs'].get('group')
        self.connect()
        # 将客户端的连接对象加入到某个地方(内存/redis)
        async_to_sync(self.channel_layer.group_add)(self.group_id, self.channel_name)

    def websocket_receive(self, message):
        # 通知组内的所有客户端, 执行xx_oo方法, 在此方法中自己可以去定义任意的功能
        message = message['text']
        async_to_sync(self.channel_layer.group_send)(self.group_id, {'type': 'message.send', 'msg': message})

    # 自定义方法, 组内通知使用
    def message_send(self, event):
        print(event)
        text = event['msg']
        self.send(text)

    def websocket_disconnect(self, message):
        # 将客户端的连接对象从组内移除
        async_to_sync(self.channel_layer.group_discard)(self.group_id, self.channel_name)
        raise StopConsumer()
'''


class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        self.group_id = self.scope['url_route']['kwargs'].get('group')
        self.groups.append(self.group_id)
        super(ChatConsumer, self).websocket_connect(self)

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            print(text_data)
            async_to_sync(self.channel_layer.group_send)(
                self.group_id,
                {'type': 'message.send', 'msg': text_data}
            )

    # 自定义方法, 组内通知使用
    def message_send(self, event):
        text = event['msg']
        self.send(text)

    def disconnect(self, code):
        pass
