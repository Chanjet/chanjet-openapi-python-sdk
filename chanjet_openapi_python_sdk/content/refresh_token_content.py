# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 13:43
# @Author  : zc
# @Desc    : 刷新开放平台token的请求参数实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 刷新开放平台token的请求参数实体
class RefreshTokenContent(ChanjetContent):

    def __init__(self, app_key, refresh_token):
        """
        刷新开放平台token的请求参数实体初始化方法
        :param app_key: 开放平台的appKey
        :type app_key: str
        :param refresh_token: 刷新令牌
        :type refresh_token: str
        """

        # 授权类型，固定填refresh_token
        self.grantType = 'refresh_token'
        self.appKey = app_key
        self.refreshToken = refresh_token
