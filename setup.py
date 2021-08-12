from setuptools import setup


with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="chanjet-openapi-python-sdk",
    version="1.0.1",
    author="zc",
    author_email="zhaochang1@chanjet.com",
    description="畅捷通开放平台python版sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Chanjet/chanjet-openapi-python-sdk",
    packages=[
        'chanjet_openapi_python_sdk',
        'chanjet_openapi_python_sdk.content',
        'chanjet_openapi_python_sdk.content.tplus',
        'chanjet_openapi_python_sdk.exception',
        'chanjet_openapi_python_sdk.request',
        'chanjet_openapi_python_sdk.request.tplus',
        'chanjet_openapi_python_sdk.response',
        'chanjet_openapi_python_sdk.response.tplus',
        'chanjet_openapi_python_sdk.utils'
    ],
    install_requires=['requests==2.26.0'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
