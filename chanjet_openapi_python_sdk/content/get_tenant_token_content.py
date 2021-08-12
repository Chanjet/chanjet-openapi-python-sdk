# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 16:32
# @Author  : zc
# @Desc    : 获取租户token请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 获取租户token请求体实体
class GetTenantTokenContent(ChanjetContent):

    def __init__(self, tenant_id, app_name, scope='auth_all'):
        """
        获取租户token实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param app_name: 畅捷通内应用名
        :type app_name: str
        :param scope: 授权范围
        :type scope: str
        """

        self.tenantId = tenant_id
        self.appName = app_name
        self.scope = scope
