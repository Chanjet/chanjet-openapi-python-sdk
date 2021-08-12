# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 15:01
# @Author  : zc
# @Desc    : 创建生凭证请求体实体
from chanjet_openapi_python_sdk.chanjet_content import ChanjetContent


# 创建生凭证请求体实体
class CreateDocContent(ChanjetContent):

    def __init__(self, voucher_date, external_code, doc_type, attached_voucher_num):
        self.dto = self.Dto(voucher_date, external_code, doc_type, attached_voucher_num)

    class Dto:

        def __init__(self, voucher_date, external_code, doc_type_code, attached_voucher_num):
            """
            凭证实体初始化方法
            :param voucher_date: 制单日期
            :type voucher_date: str
            :param external_code: 外部编码
            :type external_code: str
            :param doc_type_code: 凭证类别编码
            :type doc_type_code: str
            :param attached_voucher_num: 附单据数
            :type attached_voucher_num: str
            """

            self.VoucherDate = voucher_date
            self.ExternalCode = external_code
            self.DocType = self.DocTypeInfo(doc_type_code)
            self.AttachedVoucherNum = attached_voucher_num
            self.Entrys = []

        class DocTypeInfo:

            def __init__(self, doc_type_code):
                self.Code = doc_type_code


# 凭证明细实体
class Entry:

    def __init__(self, summary, account_code, currency_code, amount, is_cr=True):
        """
        凭证明细实体初始化方法
        :param summary: 摘要
        :type summary: str
        :param account_code: 科目编号
        :type account_code: str
        :param currency_code: 货币编号
        :type currency_code: str
        :param amount: 本币
        :type amount: str
        :param is_cr: 是否为贷方，如果为False则为借方
        :type is_cr: bool
        """

        self.Summary = summary
        self.Account = self.AccountInfo(account_code)
        self.Currency = self.CurrencyInfo(currency_code)
        if is_cr:
            self.AmountCr = amount
        else:
            self.AmountDr = amount
        self.AuxInfos = []

    class AccountInfo:

        def __init__(self, account_code):
            self.Code = account_code

    class CurrencyInfo:

        def __init__(self, currency_code):
            self.Code = currency_code


# 辅助核算项实体
class AuxInfo:

    def __init__(self, settle_style_code, bank_account_code, aux_acc_inventory_code):
        """
        辅助核算项实体初始化方法
        :param settle_style_code: 结算方式编码
        :type settle_style_code: str
        :param bank_account_code: 账号编码
        :type bank_account_code: str
        :param aux_acc_inventory_code: 存货编码
        :type aux_acc_inventory_code: str
        """

        self.SettleStyle = self.SettleStyleInfo(settle_style_code)
        self.BankAccount = self.BankAccountInfo(bank_account_code)
        self.AuxAccInventory = self.AuxAccInventoryInfo(aux_acc_inventory_code)

    class SettleStyleInfo:

        def __init__(self, settle_style_code):
            self.Code = settle_style_code

    class BankAccountInfo:

        def __init__(self, bank_account_code):
            self.Code = bank_account_code

    class AuxAccInventoryInfo:

        def __init__(self, aux_acc_inventory_code):
            self.Code = aux_acc_inventory_code
