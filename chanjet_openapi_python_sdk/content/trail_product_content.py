# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 9:54
# @Author  : zc
# @Desc    : 产品试用请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 产品试用请求体实体
class TrailProductContent(ChanjetContent):

    def __init__(self, tenant_id, product_id, agent_code, referee_name):
        """
        产品试用实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param agent_code: 服务商编码，沙箱环境传w
        :type agent_code: str
        :param referee_name: 推荐码
        :type referee_name: str
        """

        self.tenantId = tenant_id
        self.productId = product_id
        self.agentCode = agent_code
        self.refereeName = referee_name
