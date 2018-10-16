from rest_framework.views import exception_handler
import logging

# from rest_framework import exceptions
# APIException 所有异常的父类
# ParseError 解析错误
# AuthenticationFailed 认证失败
# NotAuthenticated 尚未认证
# PermissionDenied 权限决绝
# NotFound 未找到
# MethodNotAllowed 请求方式不支持
# NotAcceptable 要获取的数据格式不支持
# Throttled 超过限流次数
# ValidationError 校验失败
logger = logging.getLogger(__file__)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)

    # 在此处补充自定义的异常处理
    if response is not None:
        if isinstance(response.data, dict) and 'detail' in response.data.keys():
            response.data['error_msg'] = response.data['detail']
            del response.data['detail']
        if hasattr(exc, 'detail') and hasattr(exc.detail, 'items'):
            response.data = {}
            for key, value in exc.detail.items():
                    # append errors into the list
                response.data['error_msg'] = value[0]
                break

        response.data['status_code'] = response.status_code

    return response
