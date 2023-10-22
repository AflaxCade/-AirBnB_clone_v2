#!/usr/bin/python3
"""module for tests for class City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """tests for class City """

    def __init__(self, *args, **kwargs):
        """ tests for class City """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ tests for class City """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ tests for class City """
        new = self.value()
        self.assertEqual(type(new.name), str)
