# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 13:35
# @Author  : zc
# @Desc    : 获取企业凭证请求类
from chanjet_openapi_python_sdk.chanjet_request import ChanjetRequest


class GetOrgAccessTokenRequest(ChanjetRequest):

    def get_http_method(self):
        return 'post'
