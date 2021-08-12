# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 往来单位查询条件的请求实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 往来单位查询条件的请求实体
class QueryPartnerContent(ChanjetContent):

    def __init__(self, code, name, made_record_date):
        self.param = self.Params(code, name, made_record_date)

    class Params:

        def __init__(self, code, name, made_record_date):
            """
            往来单位查询条件实体初始化方法
            :param code: 往来单位编码
            :type code: str
            :param name: 往来单位名称
            :type name: str
            :param made_record_date: 建档日期
            :type made_record_date: str
            """

            self.Code = code
            self.Name = name
            self.MadeRecordDate = made_record_date
            self.SelectFields = 'Code,Name,ShortHand,PartnerClass.Code,PartnerClass.Name,Disabled'
