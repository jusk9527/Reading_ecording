# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     simplewggi01
   Description :
   Author :       jusk?
   date：          2019/12/25
-------------------------------------------------
   Change Activity:
                   2019/12/25:
-------------------------------------------------


上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

        environ：一个包含所有HTTP请求信息的dict对象；

        start_response：一个发送HTTP响应的函数。


{'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'WIN-8NBD2V2KP76', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Administrator', 'LIB': 'C:\\Program Files\\SQLXML 4.0\\bin\\', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'LOGONSERVER': '\\\\WIN-8NBD2V2KP76', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\Administrator\\Desktop\\env\\venv\\Scripts;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Microsoft SQL Server\\80\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\90\\DTS\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\Binn\\VSShell\\Common7\\IDE\\;C:\\Program Files (x86)\\Microsoft Visual Studio 8\\Common7\\IDE\\PrivateAssemblies\\;C:\\Program Files\\nodejs\\;D:\\Redis\\;C:\\Program Files\\Git\\bin;;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\npm;;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e09', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PT6HOME': 'E:\\思科\\Cisco Packet Tracer 6.2sv', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\bin;', 'PYCHARM_DISPLAY_PORT': '54764', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\Administrator\\Downloads\\simple_wsgi;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_matplotlib_backend;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'WIN-8NBD2V2KP76', 'USERNAME': 'Administrator', 'USERPROFILE': 'C:\\Users\\Administrator', 'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'VIRTUAL_ENV': 'C:\\Users\\Administrator\\Desktop\\env\\venv', 'WINDIR': 'C:\\Windows', '_OLD_VIRTUAL_PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\Microsoft SQL Server\\80\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\90\\DTS\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\Binn\\VSShell\\Common7\\IDE\\;C:\\Program Files (x86)\\Microsoft Visual Studio 8\\Common7\\IDE\\PrivateAssemblies\\;C:\\Program Files\\nodejs\\;D:\\Redis\\;C:\\Program Files\\Git\\bin;;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\npm;;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\bin;', '_OLD_VIRTUAL_PROMPT': '$P$G', 'SERVER_NAME': 'WIN-8NBD2V2KP76', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/favicon.ico', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_PRAGMA': 'no-cache', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', 'HTTP_ACCEPT': 'image/webp,image/apng,image/*,*/*;q=0.8', 'HTTP_REFERER': 'http://127.0.0.1:8000/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8', 'HTTP_COOKIE': 'csrftoken=Tvt0j5RmZ21lZ1nAfMhZZ1lWg8tJI2GpSxYao91KOjgKEhdBG7ckVS1AcTa4i02K; fldt=hide; remember_token=1|5ee3b4681d12f51be216c5273ffac96da334c6d43d2e28abad148b1f44dc9f4d5920abdef6331e1a56825bd4f0f2e5e00032a4c4c86904a3f8b87fa20e04e2f5', 'wsgi.input': <_io.BufferedReader name=428>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017805733037760


# 这里的我们我们可以借助python3.6自带的wsgi包进行实验
"""

from wsgiref.simple_server import make_server
if __name__ == "__main__":

    def application(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        print(environ)
        # print(start_response)
        return [b'<h1>Hello, web!</h1>']


    # server.py
    # 从wsgiref模块导入:
    # 导入我们自己编写的application函数:

    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 8000, application)
    print("Serving HTTP on port 8000...")
    # 开始监听HTTP请求:
    httpd.serve_forever()