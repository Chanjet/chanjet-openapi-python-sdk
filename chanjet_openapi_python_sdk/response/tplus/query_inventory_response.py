# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 查询存货返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class QueryInventoryResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 存货编码
        self.Code = ''
        # 存货名称
        self.Name = ''
        # 存货助记码
        self.Shorthand = ''
        # 存货分类
        self.InventoryClass = self.InventoryClassInfo()
        # 是否停用
        self.Disabled = ''
        # 是否销售属性
        self.IsSale = ''
        if data:
            self.__dict__ = data

    class InventoryClassInfo:

        def __init__(self):
            # 存货分类编码
            self.Code = ''
            # 存货分类名称
            self.Name = ''

    def __str__(self):
        return str(self.__dict__)
