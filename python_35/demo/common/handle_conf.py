"""
@Time    : 2022/4/6 20:19
@Author  : feng
"""
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')

conf = Config(r"D:\PycharmProjects\Python_C\python_35\demo\conf\config.ini")

# if __name__ == '__main__':
#     # conf = ConfigParser()
#     # conf.read(r"D:\PycharmProjects\Python_C\python_35\demo\config.ini")
#     conf = Config(r"D:\PycharmProjects\Python_C\python_35\demo\config.ini")
#     name = conf.get("logging", "name")
#     leven = conf.get("logging", "leven")
#     filname = conf.get("logging", "filname")
#     sh_leven = conf.get("logging", "sh_leven")
#     fh_leven = conf.get("logging", "fh_leven")
#     print(name)
