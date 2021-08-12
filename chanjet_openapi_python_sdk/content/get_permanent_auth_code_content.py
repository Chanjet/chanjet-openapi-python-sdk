# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 11:23
# @Author  : zc
# @Desc    : 获取企业永久授权码请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 获取企业永久授权码请求体实体
class GetPermanentAuthCodeContent(ChanjetContent):

    def __init__(self, app_access_token, temp_auth_code):
        """
        获取企业永久授权码初始化方法
        :param app_access_token: 应用凭证
        :type app_access_token: str
        :param temp_auth_code: 企业临时授权码
        :type temp_auth_code: str
        """

        self.appAccessToken = app_access_token
        self.tempAuthCode = temp_auth_code
