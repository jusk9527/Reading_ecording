import json
from channels.generic.websocket import WebsocketConsumer
from tailf.tasks import tailf


class TailfConsumer(WebsocketConsumer):
    def connect(self):
        self.file_id = self.scope["url_route"]["kwargs"]["id"]

        self.result = tailf.delay(self.file_id, self.channel_name)

        print('connect:', self.channel_name, self.result.id)
        self.accept()

    def disconnect(self, close_code):
        # 中止执行中的Task
        self.result.revoke(terminate=True)
        print('disconnect:', self.file_id, self.channel_name)

    def send_message(self, event):
        self.send(text_data=json.dumps({
            "message": event["message"]
        }))