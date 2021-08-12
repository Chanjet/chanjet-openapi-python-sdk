# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:37
# @Author  : zc
# @Desc    : 获取企业凭证返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class GetOrgAccessTokenResponse(ChanjetResponse):

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
            # 企业凭证
            self.orgAccessToken = ''
            # 畅捷通企业ID
            self.orgId = ''
            # 过期时间
            self.expireTime = 0
