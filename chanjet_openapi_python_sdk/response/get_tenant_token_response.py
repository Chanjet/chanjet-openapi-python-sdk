# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 16:40
# @Author  : zc
# @Desc    : 获取租户token返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class GetTenantTokenResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 是否成功
        self.result = ''
        # 响应内容
        self.value = self.Value()
        # 错误信息，result为true时为null
        self.error = self.Error()

        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)

    class Error:

        def __init__(self):
            # 错误码
            self.code = 0
            # 错误信息
            self.msg = ''
            # 错误提示
            self.hint = ''

    class Value:

        def __init__(self):
            # 访问令牌，开放平台请求需要传的openToken
            self.accessToken = ''
            # 刷新令牌，刷新token时需要
            self.refreshToken = ''
            # 授权范围
            self.scope = ''
            # 访问令牌过期时间，单位s
            self.expiresIn = ''
            # 畅捷通用户ID
            self.userId = ''
            # 畅捷通企业ID
            self.orgId = ''
            # 畅捷通的应用名
            self.appName = ''
            # 刷新令牌过期时间，单位s
            self.refreshExpiresIn = ''
            # T+产品部分接口需要传在Cookie中的值
            self.sid = ''
