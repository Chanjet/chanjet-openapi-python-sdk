# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:26
# @Author  : zc
# @Desc    : 获取企业凭证请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 获取企业凭证请求体实体
class GetOrgAccessTokenContent(ChanjetContent):

    def __init__(self, app_access_token, permanent_auth_code):
        """
        获取企业凭证初始化方法
        :param app_access_token: 应用凭证
        :type app_access_token: str
        :param permanent_auth_code: 企业永久授权码
        :type permanent_auth_code: str
        """

        self.appAccessToken = app_access_token
        self.permanentAuthCode = permanent_auth_code
