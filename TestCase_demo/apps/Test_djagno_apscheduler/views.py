
import time
import json
from django.http import JsonResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.views.decorators.csrf import csrf_exempt


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
@register_job(scheduler, "interval", seconds=1)
def test_job():
    time.sleep(4)
    print("I'm a test job!")
    # raise ValueError("Olala!")


# # 与前端的接口
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class AddTaskView(APIView):
#     """
#     用户动态添加任务
#     """
#
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), "default")
#
#     # 具体要执行的代码
#     def test(s):
#         print("bbb")
#
#     def post(self, request, format=None):
#         start_time = request.data.get("start_time", None)
#         try:
#             s = request.data.get("s", None)
#             start_time = start_time.split(':')
#             print(start_time)
#             hour = int(start_time[0])
#             minute = int(start_time[1])
#             second = int(start_time[2])
#
#             print(hour,minute,second)
#
#             # 创建任务
#             # scheduler.add_job(test, 'cron', hour=hour, minute=minute, second=second, args=s)
#             self.scheduler.add_job(self.test, trigger="interval", seconds=1, id="job")
#
#             code = '200'
#             message = 'success'
#
#             data = {
#                 'code': code,
#                 'message': message
#             }
#         except:
#             code = '400'
#             message = 'fail'
#             data = {
#                 'code': code,
#                 'message': message
#             }
#
#         register_events(self.scheduler)
#
#         self.scheduler.start()
#
#
#         return Response(data)




@csrf_exempt
# 与前端的接口
def test_add_task(request):
    if request.method == 'POST':
        # content = json.loads(request.body.decode())  # 接收参数
        try:
            start_time = request.POST.get('start_time')  # 用户输入的任务开始时间, '10:00:00'
            scheduler.add_job(test, trigger="interval", seconds=int(start_time), id="good", replace_existing=True)
            code = '200'
            message = 'success'
        except Exception as e:
            code = '400'
            message = e

        data = {
            'code': code,
            'message': message
        }
        return JsonResponse(json.dumps(data, ensure_ascii=False), safe=False)


# 具体要执行的代码
def test():
    print("aa")


register_events(scheduler)
scheduler.start()



