# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 通用报表查询条件的请求体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 通用报表查询条件的请求体
class QueryReportDataContent(ChanjetContent):

    def __init__(self, report_name, page_index, page_size):
        self.request = self.Request(report_name, page_index, page_size)

    class Request:

        def __init__(self, report_name, page_index, page_size):
            """
            通用报表查询条件实体初始化方法
            :param report_name: 报表名称
            :type report_name: str
            :param page_index: 当前页码
            :type page_index: int
            :param page_size: 每页显示数量
            :type page_size: int
            """

            self.ReportName = report_name
            self.PageIndex = page_index
            self.PageSize = page_size
            # 查询项
            self.SearchItems = []
            # 需要显示的栏目
            self.ReportTableColNames = 'VoucherDate,saleDeliveryCode,partnerCode,partnerName'


class SearchItem:

    def __init__(self, column_name, begin_default, begin_default_text, end_default, end_default_text):
        """
        通用报表查询项实体初始化方法
        :param column_name: 列名
        :type column_name: str
        :param begin_default: 开始默认值
        :type begin_default: str
        :param begin_default_text: 开始默认值
        :type begin_default_text: str
        :param end_default: 结束默认值
        :type end_default: str
        :param end_default_text: 结束默认值
        :type end_default_text: str
        """

        self.ColumnName = column_name
        self.BeginDefault = begin_default
        self.BeginDefaultText = begin_default_text
        self.EndDefault = end_default
        self.EndDefaultText = end_default_text
