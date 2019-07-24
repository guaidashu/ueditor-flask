"""
author songjie
"""
from app.libs.ueditor.state import State


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
