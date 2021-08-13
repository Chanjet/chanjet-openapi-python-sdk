# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 11:18
# @Author  : zc
# @Desc    : 开放平台公共部分接口的调用示例
import logging

from chanjet_openapi_python_sdk.chanjet_client import ChanjetClient
from chanjet_openapi_python_sdk.content.add_user_content import AddUserContent
from chanjet_openapi_python_sdk.content.create_order_content import CreateOrderContent
from chanjet_openapi_python_sdk.content.create_tenant_content import CreateTenantContent
from chanjet_openapi_python_sdk.content.get_app_access_token_content import GetAppAccessTokenContent
from chanjet_openapi_python_sdk.content.get_org_access_token_content import GetOrgAccessTokenContent
from chanjet_openapi_python_sdk.content.get_permanent_auth_code_content import GetPermanentAuthCodeContent
from chanjet_openapi_python_sdk.content.get_tenant_token_content import GetTenantTokenContent
from chanjet_openapi_python_sdk.content.get_token_by_permanent_code_content import GetTokenByPermanentCodeContent
from chanjet_openapi_python_sdk.content.get_user_token_content import GetUserTokenContent
from chanjet_openapi_python_sdk.content.remove_user_content import RemoveUserContent
from chanjet_openapi_python_sdk.content.trail_product_content import TrailProductContent
from chanjet_openapi_python_sdk.request.add_user_request import AddUserRequest
from chanjet_openapi_python_sdk.request.create_order_request import CreateOrderRequest
from chanjet_openapi_python_sdk.request.create_tenant_request import CreateTenantRequest
from chanjet_openapi_python_sdk.request.get_app_access_token_request import GetAppAccessTokenRequest
from chanjet_openapi_python_sdk.request.get_cia_userinfo_request import GetCIAUserinfoRequest
from chanjet_openapi_python_sdk.request.get_login_url_request import GetLoginUrlRequest
from chanjet_openapi_python_sdk.request.get_org_access_token_request import GetOrgAccessTokenRequest
from chanjet_openapi_python_sdk.request.get_permanent_auth_code_request import GetPermanentAuthCodeRequest
from chanjet_openapi_python_sdk.request.get_tenant_token_request import GetTenantTokenRequest
from chanjet_openapi_python_sdk.request.get_token_by_permanent_code_request import GetTokenByPermanentCodeRequest
from chanjet_openapi_python_sdk.request.get_token_request import GetTokenRequest
from chanjet_openapi_python_sdk.request.get_user_token_request import GetUserTokenRequest
from chanjet_openapi_python_sdk.request.refresh_token_request import RefreshTokenRequest
from chanjet_openapi_python_sdk.request.remove_user_request import RemoveUserRequest
from chanjet_openapi_python_sdk.request.trail_product_request import TrailProductRequest
from chanjet_openapi_python_sdk.response.add_user_response import AddUserResponse
from chanjet_openapi_python_sdk.response.create_order_response import CreateOrderResponse
from chanjet_openapi_python_sdk.response.create_tenant_response import CreateTenantResponse
from chanjet_openapi_python_sdk.response.get_app_access_token_response import GetAppAccessTokenResponse
from chanjet_openapi_python_sdk.response.get_cia_userinfo_response import GetCIAUserinfoResponse
from chanjet_openapi_python_sdk.response.get_login_url_response import GetLoginUrlResponse
from chanjet_openapi_python_sdk.response.get_org_access_token_response import GetOrgAccessTokenResponse
from chanjet_openapi_python_sdk.response.get_permanent_auth_code_response import GetPermanentAuthCodeResponse
from chanjet_openapi_python_sdk.response.get_tenant_token_response import GetTenantTokenResponse
from chanjet_openapi_python_sdk.response.get_token_by_permanent_code_response import GetTokenByPermanentCodeResponse
from chanjet_openapi_python_sdk.response.get_token_response import GetTokenResponse
from chanjet_openapi_python_sdk.response.get_user_token_response import GetUserTokenResponse
from chanjet_openapi_python_sdk.response.refresh_token_response import RefreshTokenResponse
from chanjet_openapi_python_sdk.response.remove_user_response import RemoveUserResponse
from chanjet_openapi_python_sdk.response.trail_product_response import TrailProductResponse
from chanjet_openapi_python_sdk.utils.chanjet_logger import ChanjetLogger


# 刷新开放平台token的示例
def refresh_token_demo(client):
    req = RefreshTokenRequest()
    req.request_uri = '/auth/refreshToken'
    params = {
        'grantType': 'refresh_token',
        'appKey': 'A5tyQHP8',
        'refreshToken': 'fd84002a8aaf44108547bc90c9ccf566'
    }
    req.add_query_params(params)
    result = client.execute(req, RefreshTokenResponse)
    return result


# 获取CIA用户信息的示例
def get_cia_userinfo_demo(client):
    req = GetCIAUserinfoRequest()
    req.request_uri = '/accounting/cia/api/v1/user'
    result = client.execute(req, GetCIAUserinfoResponse)
    return result


# 获取登录url的示例
def get_login_url_demo(client):
    req = GetLoginUrlRequest()
    req.request_uri = '/authSite/sso/getLoginUrl'
    # 业务state参数，为json字符串，需要UrlEncode
    req.add_query_params('state', '%7B%22page%22%3A%22000000%22%2C%22partnerCode%22%3A%22cjd_abc%22%7D')
    result = client.execute(req, GetLoginUrlResponse)
    return result


# 创建租户的示例
def create_tenant_demo(client):
    req = CreateTenantRequest()
    req.request_uri = '/financial/orgAndUser/createTenant'
    req.content = CreateTenantContent('test_11111111127', '测试用户1227', '测试租户名1117')
    result = client.execute(req, CreateTenantResponse)
    return result


# 企业内添加用户的示例
def add_user_demo(client):
    req = AddUserRequest()
    req.request_uri = '/financial/orgAndUser/addUser'
    req.content = AddUserContent('test_11111111127', 'user_12122', '测试租户名1117')
    result = client.execute(req, AddUserResponse)
    return result


# 企业内移除用户的示例
def remove_user_demo(client):
    req = RemoveUserRequest()
    req.request_uri = '/financial/orgAndUser/removeUser'
    req.content = RemoveUserContent('test_11111111126', 'user_12121')
    result = client.execute(req, RemoveUserResponse)
    return result


# 获取租户token的示例
def get_tenant_token_demo(client):
    req = GetTenantTokenRequest()
    req.request_uri = '/financial/auth/getTenantToken'
    req.content = GetTenantTokenContent('test_11111111126', 'accounting')
    result = client.execute(req, GetTenantTokenResponse)
    return result


# 获取用户token的示例
def get_user_token_demo(client):
    req = GetUserTokenRequest()
    req.request_uri = '/financial/auth/getUserToken'
    req.content = GetUserTokenContent('test_11111111127', 'accounting', 'user_12122')
    result = client.execute(req, GetUserTokenResponse)
    return result


# 产品试用的示例
def trail_product_demo(client):
    req = TrailProductRequest()
    req.request_uri = '/financial/order/trailProduct'
    req.content = TrailProductContent('test_11111111127', '59', 'open', '1233')
    result = client.execute(req, TrailProductResponse)
    return result


# 代客下单的示例
def create_order_demo(client):
    req = CreateOrderRequest()
    req.request_uri = '/financial/order/createOrder'
    req.content = CreateOrderContent('test_11111111127', '3961p04282', 'kfpt', '24d81a63816d457cd7d7a541dc79cee0',
                                     '5634096745A675078462D43BF58ED5F0', 'test', '221e31312312667')
    result = client.execute(req, CreateOrderResponse)
    return result


# 获取应用凭证的示例
def get_app_access_token_demo(client):
    req = GetAppAccessTokenRequest()
    req.request_uri = '/auth/appAuth/getAppAccessToken'
    req.content = GetAppAccessTokenContent('bd05ff12c9f240d3acc10f2e321c789a')
    result = client.execute(req, GetAppAccessTokenResponse)
    return result


# 获取企业永久授权码的示例
def get_permanent_auth_code_demo(client):
    req = GetPermanentAuthCodeRequest()
    req.request_uri = '/auth/orgAuth/getPermanentAuthCode'
    req.content = GetPermanentAuthCodeContent('909c1237a7cd4858a8a825afda7924bb', '961b21d4e65b4981939f2bca7fcf012b')
    result = client.execute(req, GetPermanentAuthCodeResponse)
    return result


# 获取企业凭证的示例
def get_org_access_token_demo(client):
    req = GetOrgAccessTokenRequest()
    req.request_uri = '/auth/orgAuth/getOrgAccessToken'
    req.content = GetOrgAccessTokenContent('909c1237a7cd4858a8a825afda7924bb', '961b21d4e65b4981939f2bca7fcf012b')
    result = client.execute(req, GetOrgAccessTokenResponse)
    return result


# 授权码换token的示例
def get_token_demo(client):
    req = GetTokenRequest()
    req.request_uri = '/auth/getToken'
    params = {
        'grantType': 'authorization_code',
        'appKey': 'A5tyQHP8',
        'redirectUri': 'https://t.chanjet.com',
        'code': 'ffb20d9c95e5410896c8270e49ccd43c'
    }
    req.add_query_params(params)
    result = client.execute(req, GetTokenResponse)
    return result


# 使用用户永久授权码获取token的示例
def get_token_by_permanent_code_demo(client):
    req = GetTokenByPermanentCodeRequest()
    req.request_uri = '/auth/token/getTokenByPermanentCode'
    org_access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdG9rZW4iOiJtb2NrX3Rva2VuIiwic3ViIjoiaXN2IiwiYXVkIjoiaXN2IiwibmJmIjoxNjAzNzkzMTc1LCJhcHBJZCI6IjEwNjUiLCJpc3MiOiJjaGFuamV0IiwiZXhwIjoxNjAzODAwMzc1LCJ1c2VySWQiOiI2MTAwMDQyNjc1OCIsImlhdCI6MTYwMzc5MzE3NSwib3JnSWQiOiI5MDAwMTE5ODg2MiJ9.mQOtdpMaDdHavCVAcFJtutH7_J9ol1sqD5_RfBaoAKg'
    req.content = GetTokenByPermanentCodeContent(org_access_token, 'a5610cb8148c4da8a46c9fbdf3f6ff7d')
    result = client.execute(req, GetTokenByPermanentCodeResponse)
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

    # 刷新开放平台token
    # res = refresh_token_demo(c)

    # 获取cia用户信息
    # res = get_cia_userinfo_demo(c)

    # 获取登录url
    # res = get_login_url_demo(c)

    # 创建租户
    # res = create_tenant_demo(c)

    # 企业内添加用户
    # res = add_user_demo(c)

    # 企业内移除用户
    # res = remove_user_demo(c)

    # 获取租户token
    # res = get_tenant_token_demo(c)

    # 获取用户token
    # res = get_user_token_demo(c)

    # 产品试用
    # res = trail_product_demo(c)

    # 代客下单
    # res = create_order_demo(c)

    # 获取应用凭证
    # res = get_app_access_token_demo(c)

    # 获取企业永久授权码
    # res = get_permanent_auth_code_demo(c)

    # 获取企业凭证
    # res = get_org_access_token_demo(c)

    # 授权码换token
    # res = get_token_demo(c)

    # 授权码换token
    res = get_token_by_permanent_code_demo(c)

    print(res)

    # if res.value is None:
    #     print(res.error.__dict__)
    # else:
    #     print(res.value.__dict__)
