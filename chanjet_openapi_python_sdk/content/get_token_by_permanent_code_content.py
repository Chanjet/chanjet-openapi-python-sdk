# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 16:50
# @Author  : zc
# @Desc    : 使用用户永久授权码获取token请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 使用用户永久授权码获取token请求体实体
class GetTokenByPermanentCodeContent(ChanjetContent):

    def __init__(self, org_access_token, user_auth_permanent_code):
        """
        使用用户永久授权码获取token初始化方法
        :param org_access_token: 应用凭证
        :type org_access_token: str
        :param user_auth_permanent_code: 企业永久授权码
        :type user_auth_permanent_code: str
        """

        self.orgAccessToken = org_access_token
        self.userAuthPermanentCode = user_auth_permanent_code
