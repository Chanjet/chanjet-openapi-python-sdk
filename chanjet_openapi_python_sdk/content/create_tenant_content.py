# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 15:17
# @Author  : zc
# @Desc    : 创建租户请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 创建租户请求体实体
class CreateTenantContent(ChanjetContent):

    def __init__(self, tenant_id, name, tenant_full_name):
        """
        创建租户实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param name: 创建人用户名称
        :type name: str
        :param tenant_full_name: 企业名称，全局必须唯一
        :type tenant_full_name: str
        """

        self.tenantId = tenant_id
        self.name = name
        self.tenantFullName = tenant_full_name
