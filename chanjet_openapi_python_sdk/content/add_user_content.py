# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 15:43
# @Author  : zc
# @Desc    : 企业内添加用户请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 企业内添加用户请求体实体
class AddUserContent(ChanjetContent):

    def __init__(self, tenant_id, third_platform_user_id, name):
        """
        企业内添加用户实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param third_platform_user_id: 第三方用户ID
        :type third_platform_user_id: str
        :param name: 用户名称
        :type name: str
        """

        self.tenantId = tenant_id
        self.thirdPlatformUserId = third_platform_user_id
        self.name = name

