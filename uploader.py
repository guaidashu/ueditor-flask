"""
Create by yy on 2019
"""
import imghdr
import os

from flask import current_app

from app.libs.ueditor.qiniuyun import QiNiuYun
from app.libs.ueditor.base_state import BaseState
from app.libs.ueditor.ueditor_json import UeditorJson
from tool.lib.function import md5, get_now_time_stamp, get_date_time


class Uploader(object):
    """
    文件上传类
    """

    def __init__(self, request, conf):
        self._request = request
        self._conf = conf
        self._file_path = ""
        self._file_name = ""
        self._time_stamp = get_now_time_stamp()
        self._file = self._request.files.get("file")
        self._upload_folder = current_app.config['UPLOAD_FOLDER']

    def __del__(self):
        # 删除本地图片
        os.remove(self._file_path)

    def upload(self):
        """
        上传操作
        :return:
        """
        self._file_name = self.get_file_name()
        ext = self.get_file_ext()
        self.check_upload_folder()
        self._file_path = self._upload_folder + "/" + self._file_name + ext
        self.save()
        result = self.check_type()
        if not result:
            return BaseState(False, 8)
        # 存储到七牛云
        qi_niu = QiNiuYun()
        qi_niu.save(self._file_name + ext, self._file_path)
        return self.back_data(ext)

    def get_file_name(self):
        """
        根据时间戳和文件名利用md5生成一个新的文件名
        :return:
        """
        file_name = str(self._time_stamp) + self._file.filename
        return md5(file_name)

    def get_file_ext(self):
        """
        获取文件后缀
        example: example.jpg => return .jpg
        :return:
        """
        try:
            return os.path.splitext(self._file.filename)[1]
        except ValueError:
            return ''

    def save(self):
        self._file.save(self._file_path)

    def check_upload_folder(self):
        """
        检查上传文件夹是否存在，不存在则创建
        :return:
        """
        date = get_date_time(self._time_stamp, "%Y-%m-%d")
        self._upload_folder = self._upload_folder + "/" + date
        if not os.path.exists(self._upload_folder):
            os.makedirs(self._upload_folder)
        return True

    def check_type(self):
        """
        此操作必须在调用 FileStore 的save方法后，根据
        文件的真实路径进行获取，判断后缀是否在允许列表内，
        如果是图片，则判断内容是否为真实的文件类型
        :return:
        """
        allow_file_type = current_app.config['ALLOW_FILE_TYPE']
        file_type = imghdr.what(self._file_path)
        if file_type not in allow_file_type:
            return False
        return True

    def back_data(self, ext):
        """
        包装返回的数据
        :param ext:
        :return:
        """
        ueditor = UeditorJson()
        ueditor.original = self._file_name + ext
        ueditor.url = "/" + self._file_name + ext
        ueditor.type = ext
        ueditor.state = "SUCCESS"
        ueditor.size = os.path.getsize(self._file_path)
        return ueditor
