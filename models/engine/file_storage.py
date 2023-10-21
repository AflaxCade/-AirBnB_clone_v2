#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary
        Return:
            Returns a dictionary of __objects
        """
        if not cls:
            return self.__objects
        else:
            dic_result = {}
            for key, val in self.__objects.items():
                name = key.split('.')
                if name[0] == cls.__name__:
                    dic_result.update({key: val})
            return dic_result

    def new(self, obj):
        """Sets __objects to given obj
        Args:
            obj: Given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file to objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj:
            for key in self.__objects:
                idn = key.split('.')
                if obj.id == idn[1]:
                    del self.__objects[key]
                    break
            self.save()

    def close(self):
        """
        Calls the reload() method for deserializing the JSON file to objects
        """
        self.reload()
