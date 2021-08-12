# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 通用报表查询返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class QueryReportDataResponse(ChanjetResponse):

    def __init__(self, data=None):
        self.ReportName = ''
        self.DataSource = DataSource()
        self.ColumnSource = ColumnSource()
        self.Pages = 0
        self.PageIndex = 0
        self.PageSize = 0
        self.TotalRecords = 1
        self.TaskSessionID = ''
        self.SolutionID = ''
        self.ErrorMessage = ''
        self.ErrorCode = ''
        self.ElapsedTime = 0
        self.WeakTypeDtoName = ''
        self.DtoClassName = ''
        self.IsWeakType = False
        self.AliName = ''
        self.Status = 0
        self.EnableHasChanged = False
        self.ChangedProperty = []
        self.DynamicPropertyKeys = []
        self.DynamicPropertyValues = []
        self.ID = ''
        self.DeleteID = ''
        self.Name = ''
        self.Code = ''
        self.Updated = ''
        self.UpdatedBy = ''
        self.InnerSearchLevel = 0
        self.RecordChange = True
        self.InnerPropInParentRecure = ''
        self.Ts = 0
        self.CaseSensitive = False
        self.RecordDynamicNullValue = False
        self.data = ''
        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)


class DataSource:

    def __init__(self):
        self.Rows = [self.Row()]

    class Row:

        def __init__(self):
            self.voucherdate = ''
            self.saleDeliveryCode = ''
            self.partnerCode = ''
            self.partnerName = ''
            self.GroupLevel = ''
            self.rowType = ''
            self.reportRowType = ''


class ColumnSource:

    def __init__(self):
        self.Rows = [self.Row()]

    class Row:

        def __init__(self):
            self.FieldName = ''
            self.Title = ''
            self.ParentFieldName = ''
