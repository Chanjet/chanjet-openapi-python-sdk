# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 畅捷通开放平台T+部分接口的调用示例
import logging

from chanjet_openapi_python_sdk.chanjet_client import ChanjetClient
from chanjet_openapi_python_sdk.content.tplus.create_doc_content import AuxInfo, Entry, CreateDocContent
from chanjet_openapi_python_sdk.content.tplus.create_inventory_content import CreateInventoryContent
from chanjet_openapi_python_sdk.content.tplus.create_partner_content import CreatePartnerContent
from chanjet_openapi_python_sdk.content.tplus.create_sale_delivery_contect import CreateSaleDeliveryContent, SaleDeliveryDetail
from chanjet_openapi_python_sdk.content.tplus.create_sale_order_content import SaleOrderDetail, CreateSaleOrderContent
from chanjet_openapi_python_sdk.content.tplus.query_current_stock_content import QueryCurrentStockContent
from chanjet_openapi_python_sdk.content.tplus.query_partner_content import QueryPartnerContent
from chanjet_openapi_python_sdk.content.tplus.query_report_data_content import SearchItem, QueryReportDataContent
from chanjet_openapi_python_sdk.request.tplus.create_doc_request import CreateDocRequest
from chanjet_openapi_python_sdk.request.tplus.create_inventory_request import CreateInventoryRequest
from chanjet_openapi_python_sdk.request.tplus.create_sale_delivery_request import CreateSaleDeliveryRequest
from chanjet_openapi_python_sdk.request.tplus.create_sale_order_request import CreateSaleOrderRequest
from chanjet_openapi_python_sdk.request.tplus.query_current_stock_request import QueryCurrentStockRequest
from chanjet_openapi_python_sdk.request.tplus.query_inventory_request import QueryInventoryRequest
from chanjet_openapi_python_sdk.request.tplus.query_partner_request import QueryPartnerRequest
from chanjet_openapi_python_sdk.request.tplus.query_report_data_request import QueryReportDataRequest
from chanjet_openapi_python_sdk.response.tplus.query_current_stock_response import QueryCurrentStockResponse
from chanjet_openapi_python_sdk.response.tplus.query_inventory_response import QueryInventoryResponse
from chanjet_openapi_python_sdk.content.tplus.query_inventory_content import QueryInventoryContent
from chanjet_openapi_python_sdk.response.tplus.query_partner_response import QueryPartnerResponse
from chanjet_openapi_python_sdk.response.tplus.query_report_data_response import QueryReportDataResponse
from chanjet_openapi_python_sdk.utils.chanjet_logger import ChanjetLogger


# 查询存货示例
def query_inventory_demo(client):
    req = QueryInventoryRequest()
    req.request_uri = '/tplus/api/v2/inventory/Query'
    # 推荐使用字典传值方式，直接传实体实例会有一定的性能损耗
    # req.content = {'param': {'Code': '123'}}
    req.content = QueryInventoryContent('124', '123', False, True)
    # 支持将返回值解析成实体类属性，如果不传入实体类名，则按照json的格式进行转换成字典、列表、字符串等
    result = client.execute(req, QueryInventoryResponse)
    return result


# 创建存货示例
def create_inventory_demo(client):
    req = CreateInventoryRequest()
    req.request_uri = '/tplus/api/v2/inventory/Create'
    req.content = CreateInventoryContent('01001', '中南海1mg', 'ZNH1mg', '10mg', '10', '2', '个', 'false', 'true', 'true',
                                         'true')
    # 由于该接口创建存货成功后会返回null，所以不用额外定义返回值实体
    result = client.execute(req)
    return result


# 查询往来单位示例
def query_partner_demo(client):
    req = QueryPartnerRequest()
    req.request_uri = '/tplus/api/v2/partner/Query'
    req.content = QueryPartnerContent('0010003', '往来单位03', "2021-08-05")
    result = client.execute(req, QueryPartnerResponse)
    return result


# 创建往来单位示例
def create_partner_demo(client):
    req = CreateInventoryRequest()
    req.request_uri = '/tplus/api/v2/partner/Create'
    req.content = CreatePartnerContent('00101', '河北电力公司', 'HBDLGS', '河北电力公司', '01', '001')
    result = client.execute(req)
    return result


# 创建销货单示例
def create_sale_delivery_demo(client):
    req = CreateSaleDeliveryRequest()
    req.request_uri = '/tplus/api/v2/saleDelivery/Create'
    detail = SaleDeliveryDetail('01001', '个', 5, 6.4, 90, ['priuserdefnvc1', 'priuserdefdecm1'], ['sn001', '123'])
    sale_delivery = CreateSaleDeliveryContent('2021-08-05', 'Taobao-2020061503344001', '0010001', '01', '北京市海淀区',
                                              '张三', '13611111111', ['priuserdefnvc1', 'priuserdefdecm1'], ['h001', '111'])
    sale_delivery.dto.SaleDeliveryDetails.append(detail)
    req.content = sale_delivery
    result = client.execute(req)
    return result


# 创建销货订单示例
def create_sale_order_demo(client):
    req = CreateSaleOrderRequest()
    req.request_uri = '/tplus/api/v2/saleOrder/Create'
    detail = SaleOrderDetail('01001', '个', 5, 6.4, ['priuserdefnvc1', 'priuserdefdecm1'], ['sn001', '123'])
    sale_order = CreateSaleOrderContent('2021-08-05', 'Taobao-2020061503344002', '0010001', '北京市海淀区',
                                        '张三', '13611111111', ['isautoaudit'], [True])
    sale_order.dto.SaleOrderDetails.append(detail)
    req.content = sale_order
    result = client.execute(req)
    return result


# 查询指定仓库、指定存货的现存量示例
def query_current_stock_content_demo(client):
    req = QueryCurrentStockRequest()
    req.request_uri = '/tplus/api/v2/currentStock/Query'
    req.content = QueryCurrentStockContent('0001', '01001', 20, 1, True, True, True)
    result = client.execute(req, QueryCurrentStockResponse)
    return result


# 创建凭证的示例
def create_doc_demo(client):
    req = CreateDocRequest()
    aux_info = AuxInfo('1', '0102', '01001')
    entry_cr = Entry('提现', '1001', 'RMB', '100')
    entry_dr = Entry('提现', '1002', 'RMB', '100', False)
    doc_content = CreateDocContent('2021-08-06', '1', '记', 2)
    entry_dr.AuxInfos.append(aux_info)
    doc_content.dto.Entrys.extend([entry_cr, entry_dr])
    req.request_uri = '/tplus/api/v2/doc/Create'
    req.content = doc_content
    result = client.execute(req)
    return result


# 简单报表查询
def query_report_data_demo(client):
    req = QueryReportDataRequest()
    req.request_uri = '/tplus/api/v2/reportQuery/GetReportData'
    search_item = SearchItem('VoucherDate', '2021-08-06', '2021-08-06', '2021-08-06', '2021-08-06')
    query_report_data_content = QueryReportDataContent('SA_SaleDeliveryDetailRpt', 1, 4)
    query_report_data_content.request.SearchItems.append(search_item)
    req.content = query_report_data_content
    result = client.execute(req, QueryReportDataResponse)
    return result


if __name__ == '__main__':
    # 设置自定义日志配置
    ChanjetLogger(logging.INFO)

    c = ChanjetClient('https://openapi.chanjet.com')
    # 请填入您从开放平台申请下来的appKey
    c.app_key = 'A******8'
    # 请填入您从开放平台申请下来的appSecret
    c.app_secret = '9****************8'
    # 请填入您的开放平台openToken
    c.open_token = """e****************************************************************************k"""

    # 查询存货
    # res = query_inventory_demo(c)

    # 查询往来单位
    # res = query_partner_demo(c)

    # 创建存货
    # res = create_inventory_demo(c)

    # 创建往来单位
    # res = create_partner_demo(c)

    # 创建销货单
    # res = create_sale_delivery_demo(c)

    # 创建销售订单
    # res = create_sale_order_demo(c)

    # 查询指定仓库、指定存货的现存量
    # res = query_current_stock_content_demo(c)

    # 创建凭证
    # res = create_doc_demo(c)

    # 查询报表数据
    res = query_report_data_demo(c)
    print(res)
