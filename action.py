"""
author songjie
"""
from app.libs.ueditor.action_map import ActionMap
from app.libs.ueditor.base_state import BaseState
from app.libs.ueditor.config_manager import ConfigManager
from app.libs.ueditor.uploader import Uploader


class Action(object):
    def __init__(self, request, root_path, context_path, file_name):
        """
        :param request:
        :param root_path:
        :param context_path:
        :param file_name:
        """
        self._request = request
        self._action_type = request.values.get("action")
        self.config_manager = ConfigManager.get_config_manager(root_path, context_path, file_name)

    def exec(self):
        """
        :return:
        """
        return self.invoke()

    def invoke(self):
        """
        :return:
        """
        if self._action_type in ActionMap.get_action_map():
            if self.config_manager and self.config_manager.valid():
                action_code = ActionMap.get_action_type(self._action_type)
                return self.switch(action_code)
            else:
                return BaseState(False, 102)
        else:
            return BaseState(False, 101)

    def switch(self, action_code):
        """
        根据前端传来的action模式进行选择要执行的操作并返回结果
        :param action_code:
        :return:
        """
        action = {
            0: self.get_all_config,
            1: self.upload_file,
            2: self.upload_file,
            3: self.upload_file,
            4: self.upload_file,
            5: self.catchimage,
            6: self.upload_list,
            7: self.upload_list
        }
        return action[action_code](action_code)

    def get_all_config(self, action_code):
        """
        获取所有配置文件信息
        :return:
        """
        return self.config_manager.get_all_config()

    def upload_file(self, action_code):
        """
        图片和文件上传
        :param action_code:
        :return:
        """
        conf = self.config_manager.get_config(action_code)
        state = Uploader(self._request, conf)
        return state.upload()

    def catchimage(self, action_code):
        """
        :param action_code:
        :return:
        """
        return "catchimage failed"

    def upload_list(self, action_code):
        """
        :param action_code:
        :return:
        """
        return 'upload list failed'
