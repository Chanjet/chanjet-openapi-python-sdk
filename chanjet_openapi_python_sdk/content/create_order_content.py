# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 10:18
# @Author  : zc
# @Desc    : 代客下单请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 代客下单请求体实体
class CreateOrderContent(ChanjetContent):

    def __init__(self, tenant_id, product_id, agent_pwd, agent_pay_pwd, agent_code, third_order_no, description):
        """
        代客下单实体初始化方法
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param agent_pwd: 服务商登录密码
        :type agent_pwd: str
        :param agent_pay_pwd: 服务商支付密码
        :type agent_pay_pwd: str
        :param agent_code: 服务商编码
        :type agent_code: str
        :param third_order_no: 第三方订单号
        :type third_order_no: str
        :param description: 订单描述
        :type description: str
        """

        self.tenantId = tenant_id
        self.productId = product_id
        self.agentPwd = agent_pwd
        self.agentPayPwd = agent_pay_pwd
        self.agentCode = agent_code
        self.thirdOrderNo = third_order_no
        self.description = description
