"""
@Time    : 2022/4/6 20:20
@Author  : feng
"""
import logging
from demo.common.handle_conf import conf


def creat_log(name, leven, filname, sh_leven, fh_leven):
    # --1.创建日志收集器name
    log = logging.getLogger(name)
    # --2.设置日志收集器收集日志的等级
    log.setLevel(leven)
    # --3.设置日志输出渠道

    # 日志输出至文件，创建一个日志输出的渠道（文件)
    fh = logging.FileHandler(filname, encoding='utf-8')
    # 设置输出日志的等级
    fh.setLevel(fh_leven)
    # 将输出渠道绑定到日志收集器
    log.addHandler(fh)

    # 日志输出至控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_leven)
    log.addHandler(sh)
    # --4.设置日志输出格式
    log_format = logging.Formatter('%(asctime)s--%(filename)s--%(levelname)s--%(lineno)d--%(message)s')
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    # 返回一个日志收集器
    return log


my_log = creat_log(
    name=conf.get("logging", "name"),
    leven=conf.get("logging", "leven"),
    filname=conf.get("logging", "filname"),
    sh_leven=conf.get("logging", "sh_leven"),
    fh_leven=conf.get("logging", "fh_leven"),
)
