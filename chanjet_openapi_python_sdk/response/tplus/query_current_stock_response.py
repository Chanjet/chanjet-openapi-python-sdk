# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 查询现存量返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class QueryCurrentStockResponse(ChanjetResponse):

    def __init__(self, data=None):
        self.WarehouseName = ""
        self.WarehouseCode = ""
        self.InvLocationName = ""
        self.InvLocationCode = ""
        self.InventoryCode = ""
        self.InventoryName = ""
        self.InventoryClassCode = ""
        self.InventoryClassName = ""
        self.DefaultBarCode = ""
        self.InvBarCode = ""
        self.UnitName = ""
        self.Specification = ""
        self.Brand = ""
        self.IsSingleUnit = ""
        self.AvailableQuantity = ""
        self.ExistingQuantity = ""
        self.UnitName2 = ""
        self.AvailableQuantity2 = ""
        self.ExistingQuantity2 = ""
        self.TS = ""
        self.TotalCount = ""
        self.SkuCode = ""
        self.Batch = ""
        self.ProductionDate = ""
        self.ExpiryDate = ""
        self.DynamicPropertyKeys = []
        self.DynamicPropertyTitles = []
        self.DynamicPropertyValues = []
        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)
