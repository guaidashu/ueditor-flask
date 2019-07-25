"""
Create by yy on 2019-07-24
"""
from .state import State


class UeditorJson(State):
    """
    ueditor的json格式类
    """

    def __init__(self):
        super().__init__()
        self.original = None
        self.size = None
        self.title = None
        self.type = None
        self.url = None
