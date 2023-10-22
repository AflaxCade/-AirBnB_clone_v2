#!/usr/bin/python3
""" module for tests for class BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from time import sleep


import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not relevant')
class test_basemodel(unittest.TestCase):
    """ tests for class BaseModel """

    def __init__(self, *args, **kwargs):
        """ tests for class BaseModel """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """ tests for class BaseModel """
        pass

    def tearDown(self):
        """tests for class BaseModel"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_default(self):
        """ tests for class BaseModel"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ tests for class BaseModel"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ tests for class BaseModel"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ tests for class BaseModel"""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}"
                         .format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """ tests for class BaseModel"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_one(self):
        """ tests for class BaseModel"""
        n = {'Name': 'holberton'}
        new = self.value(**n)
        self.assertEqual(new.Name, n['Name'])

    def test_kwargs_none(self):
        """ tests for class BaseModel"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ tests for class BaseModel"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ tests for class BaseModel"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ tests for class BaseModel"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        new.save()
        self.assertFalse(new.created_at == new.updated_at)
