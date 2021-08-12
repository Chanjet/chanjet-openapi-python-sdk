# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 17:05
# @Author  : zc
# @Desc    : 获取用户token请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 获取用户token请求体实体
class GetUserTokenContent(ChanjetContent):

    def __init__(self, tenant_id, app_name, third_platform_user_id, scope='auth_all'):
        """
        获取用户token实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param third_platform_user_id: 第三方用户ID
        :type third_platform_user_id: str
        :param app_name: 畅捷通内应用名
        :type app_name: str
        :param scope: 授权范围
        :type scope: str
        """

        self.tenantId = tenant_id
        self.thirdPlatformUserId = third_platform_user_id
        self.appName = app_name
        self.scope = scope
