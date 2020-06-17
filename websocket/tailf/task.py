from __future__ import absolute_import
from celery import shared_task

import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings


@shared_task
def tailf(id, channel_name):
    channel_layer = get_channel_layer()
    filename = settings.TAILF[int(id)]

    try:
        with open(filename) as f:
            f.seek(0, 2)

            while True:
                line = f.readline()

                if line:
                    print(channel_name, line)
                    async_to_sync(channel_layer.send)(
                        channel_name,
                        {
                            "type": "send.message",
                            "message": "微信公众号【运维咖啡吧】原创 版权所有 " + str(line)
                        }
                    )
                else:
                    time.sleep(0.5)
    except Exception as e:
        print(e)