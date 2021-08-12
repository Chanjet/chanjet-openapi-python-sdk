# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 查询往来单位返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class QueryPartnerResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 往来单位编码
        self.Code = ''
        # 往来单位名称
        self.Name = ''
        # 往来单位助记码
        self.ShortHand = ''
        # 往来单位分类
        self.PartnerClass = self.PartnerClassInfo()
        # 往来单位是否停用
        self.Disabled = ''
        if data:
            self.__dict__ = data

    class PartnerClassInfo:

        def __init__(self):
            # 往来单位分类编码
            self.Code = ''
            # 往来单位分类名称
            self.Name = ''

    def __str__(self):
        return str(self.__dict__)

