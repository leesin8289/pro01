from django.http import HttpResponse

#
# class MyMiddleware(object):
#
#     def __init__(self):
#         print('__init__')
#
#     def process_request(self,request):
#         """django创建request对象之后，url匹配之前"""
#         print('process_request')
#         # ip = request.META.get('REMOTE_ADDR')
#         # if ip in ['127.0.0.1']:
#         #     return HttpResponse('禁止访问')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('--process_view--')
#
#     def process_response(self, request, response):
#         """视图函数执行之后，返回内容给浏览器之前"""
#         print('--process_response--')
#         return response
    # 试图出错时调用
    # def process_exception(self, request, exception):
    #     print('-----process_exception')
    #     return HttpResponse('出错了：%s'%exception)

# class MyMiddleware2(object):
#
#     def __init__(self):
#         print('__init__2')
#
#     def process_request(self,request):
#         """django创建request对象之后，url匹配之前"""
#         print('process_request2')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('--process_view2--')
#
#     def process_response(self, request, response):
#         """视图函数执行之后，返回内容给浏览器之前"""
#         print('--process_response2--')
#         return response
# 试图出错时调用
# def process_exception(self, request, exception):
#     print('-----process_exception2')
#     return HttpResponse('出错了：%s'%exception)
