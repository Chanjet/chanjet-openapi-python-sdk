# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 11:02
# @Author  : zc
# @Desc    : 获取CIA用户信息的返回值实体
from chanjet_openapi_python_sdk.chanjet_response import ChanjetResponse


class GetCIAUserinfoResponse(ChanjetResponse):

    def __init__(self, data=None):
        # 企业类型
        self.orgType = ''
        # 企业的全称
        self.orgFullName = ''
        # 用户备注
        self.remark = ''
        # 用户类型
        self.userType = ''
        # 登录使用的账号
        self.loginAccount = ''
        # 企业ID
        self.orgId = ''
        # 用户名
        self.username = ''
        # 用户ID
        self.userId = ''
        # 最后修改时间
        self.modifyTime = ''
        # 签名
        self.signature = ''
        # 公司名
        self.companyName = ''
        # 默认的企业ID
        self.defaultOrganization = ''
        # 是否成功
        self.result = True
        # 创建时间
        self.createTime = ''
        # 头像
        self.headPicture = ''
        # 推广来源
        self.origin = ''
        # 企业简称
        self.orgName = ''
        # 修改的次数
        self.userVersion = ''
        # 和userId一样
        self.userLongId = ''

        if data:
            self.__dict__ = data

    def __str__(self):
        return str(self.__dict__)
