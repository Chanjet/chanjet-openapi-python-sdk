# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 现存量查询条件的请求实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 现存量查询条件的请求实体
class QueryCurrentStockContent(ChanjetContent):

    def __init__(self, code, name, warehouse_code, inventory_code, is_warehouse, is_inventory, is_inv_property):
        self.param = self.Params(code, name, warehouse_code, inventory_code, is_warehouse, is_inventory, is_inv_property)

    class Params:

        def __init__(self, warehouse_code, inventory_code, page_size, page_index, is_warehouse, is_inventory, is_inv_property):
            """
            现存量查询条件实体初始化方法
            :param warehouse_code: 仓库编码
            :type warehouse_code: str
            :param inventory_code: 存货编码
            :type inventory_code: str
            :param page_size: 分页查询每页数量
            :type page_size: int
            :param page_index: 分页查询的页号
            :type page_index: int
            :param is_warehouse: 是否按照仓库分组
            :type is_warehouse: bool
            :param is_inventory: 是否按照存货分组
            :type is_inventory: bool
            :param is_inv_property: 是否按照销售属性分组
            :type is_inv_property: bool
            """

            self.Warehouse = [self.WarehouseInfo(warehouse_code)]
            self.Inventory = [self.InventoryInfo(inventory_code)]
            self.PageSize = page_size
            self.PageIndex = page_index
            self.GroupInfo = self.GroupList(is_warehouse, is_inventory, is_inv_property)

        class WarehouseInfo:

            def __init__(self, warehouse_code):
                self.Code = warehouse_code

        class InventoryInfo:

            def __init__(self, inventory_code):
                self.Code = inventory_code

        class GroupList:

            def __init__(self, is_warehouse, is_inventory, is_inv_property):
                self.Warehouse = is_warehouse
                self.Inventory = is_inventory
                self.InvProperty = is_inv_property
