"""
author songjie
"""


class AppInfo(object):
    _app_info = {
        0: "SUCCESS",
        101: "无效的Action",
        102: "配置文件初始化失败",
        203: "抓取远程图片失败",
        201: "被阻止的远程主机",
        202: "远程连接出错",
        1: "文件大小超出限制",
        2: "权限不足",
        3: "创建文件失败",
        4: "IO错误",
        5: "上传表单不是multipart/form-data类型",
        6: "解析上传表单错误",
        7: "未找到上传数据",
        8: "不允许的文件类型",
        301: "指定路径不是目录",
        302: "指定路径并不存在",
        401: "Callback参数名不合法"
    }

    @classmethod
    def get_state_info(cls, key):
        return cls._app_info[key]
