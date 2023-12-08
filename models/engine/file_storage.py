#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(save_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                load_dict = json.load(f)
                for key, value in load_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
