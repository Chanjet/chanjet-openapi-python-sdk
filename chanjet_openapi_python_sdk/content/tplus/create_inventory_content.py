# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 创建存货请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 创建存货请求体实体
class CreateInventoryContent(ChanjetContent):

    def __init__(self, code, name, shorthand, specification, inventory_class_code, unit_code, unit_name, disabled,
                 is_single_unit, is_purchase, is_sale):
        self.dto = self.Dto(code, name, shorthand, specification, inventory_class_code, unit_code, unit_name, disabled,
                            is_single_unit, is_purchase, is_sale)

    class Dto:

        def __init__(self, code, name, shorthand, specification, inventory_class_code, unit_code, unit_name, disabled,
                     is_single_unit, is_purchase, is_sale):
            """
            存货实体初始化方法
            :param code: 存货编码
            :type code: str
            :param name: 存货名称
            :type name: str
            :param shorthand: 助记码
            :type shorthand: str
            :param specification: 规格型号
            :type specification: str
            :param inventory_class_code: 存货分类编码
            :type inventory_class_code: str
            :param unit_code: 计量单位编码
            :type unit_code: str
            :param unit_name: 计量单位名
            :type unit_name: str
            :param disabled: 是否停用
            :type disabled: str
            :param is_single_unit: 是否单计量
            :type is_single_unit: str
            :param is_purchase: 是否外购
            :type is_purchase: str
            :param is_sale: 是否销售
            :type is_sale: str
            """

            self.Code = code
            self.Name = name
            self.Shorthand = shorthand
            self.Specification = specification
            self.InventoryClass = self.InventoryClassInfo(inventory_class_code)
            self.Unit = self.UnitInfo(unit_code, unit_name)
            self.Disabled = disabled
            self.IsSingleUnit = is_single_unit
            self.IsPurchase = is_purchase
            self.IsSale = is_sale

        class InventoryClassInfo:

            def __init__(self, inventory_class_code):
                self.Code = inventory_class_code

        class UnitInfo:

            def __init__(self, unit_code, unit_name):
                self.Code = unit_code
                self.Name = unit_name
