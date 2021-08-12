# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 存货查询条件的请求实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 存货查询条件的请求实体
class QueryInventoryContent(ChanjetContent):

    def __init__(self, code, inventory_class_code, is_stop, is_sale):
        self.param = self.Params(code, inventory_class_code, is_stop, is_sale)

    class Params:

        def __init__(self, code, inventory_class_code, is_stop, is_sale):
            """
            存货查询条件实体初始化方法
            :param code: 存货编码
            :type code: str
            :param inventory_class_code: 存货分类编码
            :type inventory_class_code: str
            :param is_stop: 是否停用
            :type is_stop: bool
            :param is_sale: 是否销售属性
            :type is_sale: bool
            """

            self.Code = code
            self.InventoryClass = self.InventoryClassInfo(inventory_class_code)
            self.Disabled = is_stop
            self.IsSale = is_sale
            # 需要返回的字段名
            self.SelectFields = 'Code,Name,Shorthand,InventoryClass.Code,InventoryClass.Name,Disabled,IsSale'

        class InventoryClassInfo:

            def __init__(self, code):
                self.Code = code
