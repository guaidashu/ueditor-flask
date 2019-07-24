"""
author songjie
"""
import json
import re


class ConfigManager(object):
    """
    配置类，用以初始化配置和获取配置(从config.json获取)
    """

    def __init__(self, root_path, context_path, file_name):
        """
        构造函数
        :param root_path:
        :param context_path:
        :param file_name:
        """
        self._root_path = root_path
        self._context_path = context_path
        self._file_name = file_name
        self._json_config = None
        self.init_env()

    def get_config(self, t):
        """
        根据键值获取配置
        :param t:
        :return:
        """
        pass

    @staticmethod
    def get_config_manager(root_path, context_path, file_name):
        """
        工厂模式获取配置管理器实例
        :param root_path:
        :param context_path:
        :param file_name:
        :return:
        """
        try:
            return ConfigManager(root_path, context_path, file_name)
        except GeneratorExit:
            return None

    def get_all_config(self):
        """
        获取所有配置信息
        :return:
        """
        return self._json_config

    def valid(self):
        """
        判断配置是否初始化成功
        :return:
        """
        return self._json_config is not None

    def init_env(self):
        """
        初始化整个配置文件，转为json格式
        :return:
        """
        path = self._root_path + self._context_path + "/" + self._file_name
        json_content = self.read_file(path)
        self._json_config = json.loads(json_content)

    def read_file(self, path):
        """
        读取配置文件内容
        :param path:
        :return:
        """
        with open(path, "rb") as f:
            data = f.read().decode("utf-8")
            f.close()
        return self.__filter(data)

    @classmethod
    def __filter(cls, content):
        """
        过滤读取到的文件内容
        :param content:
        :return:
        """
        return re.sub("/\\*[\\s\\S]*?\\*/", "", content)
