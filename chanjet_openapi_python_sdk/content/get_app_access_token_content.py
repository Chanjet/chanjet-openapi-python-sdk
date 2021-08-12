# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:54
# @Author  : zc
# @Desc    : 获取应用凭证请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 获取应用凭证请求体实体
class GetAppAccessTokenContent(ChanjetContent):

    def __init__(self, app_ticket):
        """
        获取应用凭证实体初始化方法
        :param app_ticket: 应用票据
        :type app_ticket: str
        """

        self.appTicket = app_ticket
