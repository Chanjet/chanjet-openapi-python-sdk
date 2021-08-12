# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 创建往来单位请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 创建往来单位请求体实体
class CreatePartnerContent(ChanjetContent):

    def __init__(self, code, name, shorthand, partner_abb_name, partner_type_code, partner_class_code):
        self.dto = self.Dto(code, name, shorthand, partner_abb_name, partner_type_code, partner_class_code)

    class Dto:

        def __init__(self, code, name, shorthand, partner_abb_name, partner_type_code, partner_class_code):
            """
            往来单位实体初始化方法
            :param code: 往来单位编码
            :type code: str
            :param name: 往来单位名称
            :type name: str
            :param shorthand: 助记码
            :type shorthand: str
            :param partner_abb_name: 简称
            :type partner_abb_name: str
            :param partner_type_code: 往来单位性质编码
            :type partner_type_code: str
            :param partner_class_code: 往来单位所属类别编码
            :type partner_class_code: str
            """

            self.Code = code
            self.Name = name
            self.Shorthand = shorthand
            self.PartnerAbbName = partner_abb_name
            self.PartnerType = self.PartnerTypeInfo(partner_type_code)
            self.PartnerClass = self.PartnerClassInfo(partner_class_code)

        class PartnerClassInfo:

            def __init__(self, partner_class_code):
                self.Code = partner_class_code

        class PartnerTypeInfo:

            def __init__(self, partner_type_code):
                self.Code = partner_type_code
