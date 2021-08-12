# chanjet-open-sdk

欢迎使用 Chanjet Open SDK for Python

## 环境要求
1. Chanjet Open SDK for Python 需要配合`Python 3.8`或其以上版本。

2. 使用 Chanjet Open SDK for Python 之前 ，您需要先前往[畅捷通-开发者中心](https://dev.chanjet.com)完成开发者接入的一些准备工作，包括创建应用、获取应用的appKey和appSecret。

## 安装依赖
推荐通过pip下载
```text
pip install -i https://pypi.org/simple/ chanjet-openapi-python-sdk
```
## 快速使用

```python
import logging

from chanjet_openapi_python_sdk.chanjet_client import ChanjetClient
from chanjet_openapi_python_sdk.request.tplus.query_inventory_request import QueryInventoryRequest
from chanjet_openapi_python_sdk.response.tplus.query_inventory_response import QueryInventoryResponse
from chanjet_openapi_python_sdk.content.tplus.query_inventory_content import QueryInventoryContent
from chanjet_openapi_python_sdk.utils.chanjet_logger import ChanjetLogger


def query_inventory_demo():
    req = QueryInventoryRequest()
    req.request_uri = '/tplus/api/v2/inventory/Query'
    # 推荐使用字典传值方式，直接传实体实例会有一定的性能损耗
    # req.content = {'param': {'Code': '123'}}
    req.content = QueryInventoryContent('124', '123', False, True)
    # 支持将返回值解析成实体类属性，如果不传入实体类名，则按照json的格式进行转换成字典、列表、字符串等
    result = client.execute(req, QueryInventoryResponse)
    return result

if __name__ == '__main__':
    # 设置自定义日志配置
    ChanjetLogger(logging.INFO)

    client = ChanjetClient('https://openapi.chanjet.com')
    client.app_key = 'A5tyQHP8'
    client.app_secret = '9C910520463F2A473ABA9CE8507004D8'
    client.open_token = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdG9rZW4iOiIwNDcyNDhjYS04MjRmLTRiMDEtODFjYi0zOWE3ZTkxYzdiZmUiLCJzdWIiOiJpc3YiLCJhdWQiOiJpc3YiLCJuYmYiOjE2Mjc5NTkyOTEsImFwcElkIjoiNTgiLCJzY29wZSI6ImF1dGhfYWxsIiwiaXNzIjoiY2hhbmpldCIsImV4cCI6MTYyODQ3NzY5MSwidXNlcklkIjoiNjAwMTIzOTUzNjgiLCJpYXQiOjE2Mjc5NTkyOTEsIm9yZ0lkIjoiOTAwMTY0ODg5NzciLCJvcmdBY2NvdW50IjoidTdycnhpaGM5MHU1In0.ffmyeTcm1VK5B5ZSiefECBoGZ9fV9Hk_lWVMX3ldspk"""

    # 查询存货
    res = query_inventory_demo()
```