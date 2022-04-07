"""
@Time    : 2022/4/6 20:20
@Author  : feng
"""
import os
# 项目根目录绝对路径
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 用例数据
DATA_DIR =os.path.join(BASE_DIR,'datas')
# 配置文件
CONF_DIR =os.path.join(BASE_DIR,'conf')
# 日志文件
LOG_DIR =os.path.join(BASE_DIR,'logs')
# 报告文件
REPORT_DIR =os.path.join(BASE_DIR,'reports')
# 用力模块文件
CASES_DIR =os.path.join(BASE_DIR,'testcases')

