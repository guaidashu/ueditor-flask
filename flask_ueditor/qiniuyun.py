"""
Create by yy on 2019
"""
from flask import current_app
from qiniu import Auth, put_file


class QiNiuYun(object):
    """
    七牛云存储包装类
    """

    def __init__(self):
        """
        这里需要初始化 access_key 和 secure_key
        """
        self._access_key = current_app.config['QINIU_ACCESS_KEY']
        self._secure_key = current_app.config['QINIU_SECURE_KEY']
        self._qi_niu = self.__init()
        self._bucket_name = current_app.config['QINIU_BUCKET_NAME']

    def __init(self):
        """
        实例化七牛云 对象
        :return:
        """
        return Auth(self._access_key, self._secure_key)

    def save(self, file_name, path):
        """
        存储文件
        :param path:
        :param file_name:
        :return:
        """
        token = self._qi_niu.upload_token(self._bucket_name, file_name, 3600)
        return put_file(token, file_name, path)
