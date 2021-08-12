# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 16:40
# @Author  : zc
# @Desc    : 授权码换token返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class GetTokenResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 错误码，200为成功，其余均为失败
        self.code = ''
        # 错误提示信息
        self.message = ''
        # 返回结果
        self.result = self.Result()

        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)

    class Result:

        def __init__(self):
            # 访问令牌
            self.access_token = ''
            # 过期时间，单位s
            self.expires_in = 0
            # 更新令牌
            self.refresh_token = ''
            # 更新令牌过期时间，单位s
            self.refresh_expires_in = 0
            # 授权域
            self.scope = ''
            # 用户ID
            self.user_id = ''
            # 企业ID
            self.org_id = ''
            # 应用名
            self.app_name = ''
            # T+产品部分接口需要传在Cookie中的值
            self.sid = ''
            # 用户永久授权码
            self.user_auth_permanent_code = ''
