#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():

    """
        Prvate class attributes
    """
    __file_path = "file.json" #path to the json file
    __objects = {} # will store all objects by class_name.id

    """
        Public class attributes and methods
    """
    def all(self):
        """
            Return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key obj-classname.id
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
            serializes __objects to th JSON file (path: __file_path)
        """
        dict_cp = {}
       
        for k, v in FileStorage.__objects.items():
            dict_cp[k] = v.to_dict()
            print("pasa")
	
        print(BaseModel)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dict_cp))
        #print(dict_cp)
	

    def reload(self):
        """
            deserializes the JSON fle to __objects (only if the JSON f            ile (__file_path) exists ; otherwise, do nothing. If the f            ile does not exist, no exception should be raised)
        """
        pass
