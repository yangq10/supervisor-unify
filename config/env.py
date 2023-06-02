"""
项目统一环境配置
"""
import os

ENV = os.environ.get('ENV', 'develop')

print("ENV:", ENV)