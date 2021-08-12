# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 创建销售订单的请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 创建销售订单的请求体实体
class CreateSaleOrderContent(ChanjetContent):

    def __init__(self, voucher_date, external_code, customer_code, address, link_man, contact_phone,
                 header_dynamic_property_keys, header_dynamic_property_values):
        self.dto = self.Dto(voucher_date, external_code, customer_code, address, link_man, contact_phone,
                            header_dynamic_property_keys, header_dynamic_property_values)

    class Dto:

        def __init__(self, voucher_date, external_code, customer_code, address, link_man, contact_phone,
                     header_dynamic_property_keys, header_dynamic_property_values):
            """
            销售订单实体初始化方法
            :param voucher_date: 单据日期
            :type voucher_date: str
            :param external_code: 外部系统单据编码
            :type external_code: str
            :param customer_code: 客户编码
            :type customer_code: str
            :param address: 送货地址
            :type address: str
            :param link_man: 联系人
            :type link_man: str
            :param contact_phone: 联系电话
            :type contact_phone: str
            :param header_dynamic_property_keys: 表头动态属性
            :type header_dynamic_property_keys: list
            :param header_dynamic_property_values: 表头动态属性值
            :type header_dynamic_property_values: list
            """

            self.VoucherDate = voucher_date
            self.ExternalCode = external_code
            self.Customer = self.CustomerInfo(customer_code)
            self.Address = address
            self.LinkMan = link_man
            self.ContactPhone = contact_phone
            self.DynamicPropertyKeys = header_dynamic_property_keys
            self.DynamicPropertyValues = header_dynamic_property_values
            self.SaleOrderDetails = []

        class CustomerInfo:

            def __init__(self, customer_code):
                self.Code = customer_code

        class InvoiceTypeInfo:

            def __init__(self, invoice_type_code):
                self.Code = invoice_type_code


# 销售订单明细实体
class SaleOrderDetail:

    def __init__(self, inventory_code, unit_name, quantity, orig_discount_price, detail_dynamic_property_keys, detail_dynamic_property_values):
        """
        销售订单明细实体初始化方法
        :param inventory_code: 存货编码
        :type inventory_code: str
        :param unit_name: 计量单位名称
        :type unit_name: str
        :param quantity: 数量
        :type quantity: float
        :param orig_discount_price: 原币单价
        :type orig_discount_price: float
        :param detail_dynamic_property_keys: 明细行动态属性
        :type detail_dynamic_property_keys: list
        :param detail_dynamic_property_values: 明细行动态属性值
        :type detail_dynamic_property_values: list
        """

        self.Inventory = self.InventoryInfo(inventory_code)
        self.Unit = self.UnitInfo(unit_name)
        self.Quantity = quantity
        self.OrigDiscountPrice = orig_discount_price
        self.DynamicPropertyKeys = detail_dynamic_property_keys
        self.DynamicPropertyValues = detail_dynamic_property_values

    class InventoryInfo:

        def __init__(self, inventory_code):
            self.Code = inventory_code

    class UnitInfo:

        def __init__(self, unit_name):
            self.Name = unit_name
