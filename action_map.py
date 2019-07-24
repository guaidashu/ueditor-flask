"""
author songjie
"""


class ActionMap(object):
    _action_map = {
        "config": 0,
        "uploadimage": 1,
        "uploadscrawl": 2,
        "uploadvideo": 3,
        "uploadfile": 4,
        "catchimage": 5,
        "listfile": 6,
        "listimage": 7
    }

    def __init__(self):
        pass

    @classmethod
    def get_action_map(cls):
        return cls._action_map

    @classmethod
    def get_action_type(cls, key):
        return cls._action_map[key]
