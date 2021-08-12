# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 14:05
# @Author  : zc
# @Desc    : 刷新开放平台token的返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class RefreshTokenResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 返回code码，200为成功，其余均为失败
        self.code = ''
        # 描述信息
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
            self.expires_in = ''
            # 更新令牌
            self.refresh_token = ''
            # 更新令牌过期时间，单位s
            self.refresh_expires_in = ''
            # 授权域
            self.scope = ''
            # 用户ID
            self.user_id = ''
            # 企业ID
            self.org_id = ''
            # 应用名
            self.app_name = ''
            # T + 产品部分接口需要传在Cookie中的值
            self.sid = ''
